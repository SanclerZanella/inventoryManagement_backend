function openModal(button, modal) {
    const modalElement = $(modal);

    $(document).on('click', button, (e) => {
        modalElement.show(500);
    });

    const span = $('.close');
    span.click(() => {
        modalElement.hide(500);
    });

    $(window).click((e) => {
        if (e.target.id == modalElement.attr('id')) {
            modalElement.hide(500);
        };
    });
};

openModal('.addItemBtn', '#addNewItemModal');

$(document).on('click', '.removeBtn', (e) => {
  modal_button = e.target;
  rm_modal = $(modal_button).data('modal');

  $(rm_modal).show(500);

  const span = $('.close');
  span.click(() => {
      $(rm_modal).hide(500);
  });

  $(window).click((e) => {
      if (e.target.id == $(rm_modal).attr('id')) {
          $(rm_modal).hide(500);
      };
  });
  
});