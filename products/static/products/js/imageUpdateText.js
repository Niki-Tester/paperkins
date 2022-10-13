$('#new-image').change(() => {
    const file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
})