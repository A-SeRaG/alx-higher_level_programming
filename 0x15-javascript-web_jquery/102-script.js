//fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
    $('#btn_translate').click(function() {
        var langCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
