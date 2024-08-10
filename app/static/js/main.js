console.log('main.js loaded (text-only version)');

(function($) {
    $(function() {
        console.log('Document ready');
        let conversationHistory = [];

        function addMessage(sender, message) {
            console.log('Adding message:', sender, message);
            var messageClass = sender === '您' ? 'user-message' : 'assistant-message';
            var messageElement = $(`<div class="message ${messageClass}"><strong>${sender}:</strong> ${message}</div>`);

            conversationHistory.push({sender: sender, message: message});

            $('#chat-box').append(messageElement);
            $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
        }

        function sendMessage() {
            console.log('Sending message');
            var userInput = $('#user-input').val();
            if (userInput.trim() === '') return;

            addMessage('您', userInput);
            $('#user-input').val('');

            $.ajax({
                url: '/process_input',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ user_input: userInput }),
                success: function(response) {
                    console.log('Server response:', response);
                    addMessage('助手', response.response);
                    if (response.order_complete) {
                        addMessage('系统', '订单已完成。您可以开始新的订单。');
                    }
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.error("AJAX error: " + textStatus + ' : ' + errorThrown);
                    addMessage('系统', '抱歉，发生了一个错误。请稍后再试。');
                }
            });
        }

        $('#send-button').on('click', function(e) {
            e.preventDefault();
            console.log('Send button clicked');
            sendMessage();
        });

        $('#user-input').on('keypress', function(e) {
            if (e.which == 13) {
                console.log('Enter key pressed');
                sendMessage();
                return false;
            }
        });

        addMessage('助手', '欢迎使用咖啡订购助手。今天想来点什么？请输入您的订单。');
    });
})(jQuery);