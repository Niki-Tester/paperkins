// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    const closestInput = $(this).closest('.input-group').find('.qty-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue += 1);
    $(this).prop('disabled', currentValue >= closestInput.max)
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    const closestInput = $(this).closest('.input-group').find('.qty-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue -= 1);
    $(this).prop('disabled', currentValue <= closestInput.min)
});

allDec = $('.decrement-qty')
for (let i = 0; i < allDec.length; i++) {
    const closestInput = $(allDec[i]).closest('.input-group').find('.qty-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(allDec[i]).prop('disabled', currentValue <= closestInput.min)
}

allInc = $('.increment-qty')
for (let i = 0; i < allInc.length; i++) {
    const closestInput = $(allInc[i]).closest('.input-group').find('.qty-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(allInc[i]).prop('disabled', currentValue >= closestInput.max)
}