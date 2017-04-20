$(function(){
  var mousedOver = false;
  if($("#imageModal").length == 0) {
    $('body').append('<div id="imageModal" class="modal">' + 
        '<span  class="close">&times;</span><img><div id="caption"></div>' + 
        '</div>');
  }

  function openModal(image) {
    $('#imageModal').css('display', 'block');
    $('#imageModal img').attr('src', $(image).attr('src'));
    $('#caption').html($(image).attr('alt'));
    mousedOver = false;
  }
  
  function closeModal() {
    $('#imageModal').css('display', 'none');
  }
  
  $('.thumbnail').click(function() {
    openModal(this);
  });
  
  $('.close').click(function(){
    closeModal();
  });
  $('#imageModal').click(function(){
    closeModal();
  });
  /* 
  $('.thumbnail').hover(function() {
    openModal(this);
  });
  
  $('#imageModal img').mouseover(function() { mousedOver = true;});
  $('#imageModal img').mouseleave(function() {
    if (mousedOver) closeModal();
  });
  */
});

