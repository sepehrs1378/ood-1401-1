var selected_channel = null;
var selected_contact_name = null;
const chatbox_interval = setInterval(update_chatbox, 1000)

async function update_chatbox() {
    if (selected_channel != null) {
        // Fetch messages
        let xml_req = new XMLHttpRequest();
        xml_req.onreadystatechange = function () {
            if (xml_req.readyState === 4) {
                // Update messages in browser
                messages = JSON.parse(xml_req.response)
                let chatbox = document.getElementById('chat');
                chatbox.innerHTML = '';
                for (let i = 0; i < messages.length; i++) {
                    msg = messages[i];
                    msg_html = `<li class="${msg['is_sent_by_me'] ? 'me' : 'you'}">
				                    <div class="entete">
					                    <h3>${msg['time']}</h3>
				                    </div>
				                    <!-- <div class="triangle"></div> -->
				                    <div class="message">
                                        ${msg['text']}
                                    </div>
			                    </li>`
                    chatbox.innerHTML += msg_html;
                }
            }
        }
        xml_req.open("GET", `/messaging/chatroom/channel/${selected_channel}/get-messages/`);
        xml_req.send(null);
    }
}

function set_selected_channel(ch, contact_name) {
    selected_channel = ch;
    selected_contact_name = contact_name;

    // Update contact name
    contact_name_header = document.getElementById('contact-name');
    contact_name_header.innerHTML = contact_name;

    update_chatbox();
}
