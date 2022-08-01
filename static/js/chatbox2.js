var selected_channel = null
const chatbox_interval = setInterval(update_chatbox, 1000)

async function update_chatbox() {
    if (selected_channel != null) {
        let xml_req = new XMLHttpRequest();
        xml_req.onreadystatechange = function () {
            if (xml_req.readyState === 4) {
                messages = JSON.parse(xml_req.response)
                let chatbox = document.getElementById("chat");
                chatbox.innerHTML = '';
                for (let i = 0; i < messages.length; i++) {
                    msg = messages[i];
                    msg_html = `<li class="you">
				                    <div class="entete">
					                    <span class="status green"></span>
					                    <h2>Vincent</h2>
					                    <h3>${msg['time']}</h3>
				                    </div>
				                    <div class="triangle"></div>
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

function set_selected_channel(ch) {
    selected_channel = ch;
    update_chatbox();
}
