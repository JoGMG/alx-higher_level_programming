// A JavaScript script that fetches and lists the title for all movies by
// using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// - All movie titles must be list in the HTML tag UL#list_movies
// - You can’t use document.querySelector to select the HTML tag
// - You must use the JQuery API

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    const films = data.results;
    films.forEach(function (film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
