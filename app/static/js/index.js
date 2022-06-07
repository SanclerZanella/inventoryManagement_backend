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
// openModal('.addItemBtn', '#removeItemModal');