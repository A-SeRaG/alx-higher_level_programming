//fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
    function fetchHello() {
        var langCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(function() {
        fetchHello();
    });

    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key pressed
            fetchHello();
        }
    });
});
