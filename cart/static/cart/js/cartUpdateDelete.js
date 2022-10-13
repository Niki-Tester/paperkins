// Update Quantity on Click
$('.update-link').click(e => {
    e.preventDefault()
    const form = $(e.currentTarget).prev('.update-form');
    form.submit();
})

// Remove item and reload on Click
$('.remove-link').click(e => {
    e.preventDefault()
    const itemId = $(e.currentTarget).attr('id').split('remove_')[1];
    const customMessage = $(e.currentTarget).data('customMessage');
    const url = `remove/${itemId}`
    let data = {}
    if (customMessage || customMessage == '') {
        data = {
            'csrfmiddlewaretoken': csrftoken,
            'custom_message': customMessage,
        }
    } else {
        data = {
            'csrfmiddlewaretoken': csrftoken,
        }
    }

    $.post(url, data)
        .done(() => {
            location.reload()
        })
})