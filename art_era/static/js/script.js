$(document).ready(function(){
    
  $('.user-menu__avatar').click(function () {
      $('.user-toggle-menu').hide();
      $(this).next().show();
      return false;
  });
  $('.page').click(function () {
      $('.user-toggle-menu').hide();
  });


  $('.user-gallery__grid').masonry({
    // options
    itemSelector: '.user-gallery__picture',
    gutter: 10
  });

// Дата пикер для страницы картины - форма Выставить ордер
  $('#data-ordera').datepicker({
    // Можно выбрать тольо даты, идущие за сегодняшним днем, включая сегодня
    minDate: new Date()
  })


// Выпадающиее меню для фильтров на странице поиска
var res = $(".dropdown-menu");
$('[rel^="m"]').on("click", funk);

$(document).click(function(e) {
  if ($(e.target).closest(res).length || $(e.target).closest('.knop').length) return;
  res.fadeOut(100);
  // e.stopPropagation();
});

function funk(){
  var link = $(this).attr('rel'),
      el = $('.dropdown-menu.'+link);
  if(el.css("display") == "none"){
    res.hide();
    el.fadeIn(100);
  }
  else{
    el.fadeOut(100);
  }
}


// Датапикер для страницы поиска - фильтр дата
 $('#data-kartina').datepicker({
    // Можно выбрать тольо даты, идущие за сегодняшним днем, включая сегодня
    minDate: new Date()
  })


});