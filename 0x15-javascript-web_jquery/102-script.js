// A JavaScript script that fetches and prints how to say “Hello”
// depending on the language
// - You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// - The language code will be the value entered in the tag
//   INPUT#language_code (ex: es, fr, en etc.)
// - The translation must be fetched when the user clicks on
//   INPUT#btn_translate
// - The translation of “Hello” must be displayed in the HTML
//   tag DIV#hello
// - You can’t use document.querySelector to select the HTML tag
// - You must use the JQuery API
// - You script must work when imported from the <head> tag

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();

    $.ajax({
      type: 'POST',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
      success: function (response) {
        $('DIV#hello').html(response.hello);
      },
      error: function (error) {
        console.log(error);
      }
    });
  });
});
