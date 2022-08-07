var selected_channel = null;
var selected_contact_name = null;
var is_for_chat = null;
const chatbox_interval = setInterval(update_chatbox, 1000)

async function update_chatbox() {
    if (selected_channel != null) {
        // Fetch messages
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                // Update messages in browser
                messages = JSON.parse(xhr.response)
                let chatbox = document.getElementById('chat');
                chatbox.innerHTML = '';
                for (let i = 0; i < messages.length; i++) {
                    msg = messages[i];
                    msg_html = `<li class="${msg["is_sent_by_me"] ? "me" : "you"}">
				                    <div class="entete">
					                    <h3>${msg["time"]}</h3>
				                    </div>
				                    <div class="message">
                                        ${msg["text"]}
                                    </div>
			                    </li>`
                    chatbox.innerHTML += msg_html;
                }
            }
        }

        if (is_for_chat) {
            xhr.open("GET", `/messaging/chatroom/channel/${selected_channel}/get-messages/`);
        }
        else {
            xhr.open("GET", `/messaging/ticket/${selected_channel}/get-messages/`);
        }
        xhr.send(null);
    }
}

function send_message() {
    if (selected_channel != null) {
        // Send message
        msg = document.getElementById("msg-text").value;

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                update_chatbox();
            }
        }

        body = `text:${msg}`;
        if (is_for_chat) {
            xhr.open("POST", `/messaging/chatroom/channel/${selected_channel}/send/`);
        }
        else {
            xhr.open("POST", `/messaging/ticket/${selected_channel}/send/`);
        }
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send(body);
    }
}

function set_selected_channel(ch, contact_name) {
    selected_channel = ch;
    selected_contact_name = contact_name;

    // Update contact name
    contact_name_header = document.getElementById('chat-header');
    contact_name_header.innerHTML = contact_name;

    update_chatbox();
}

function set_is_for_chat(bool) {
    is_for_chat = bool;
}
