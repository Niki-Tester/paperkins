const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7v4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', {
    style: style
});

card.mount('#card-element')

card.addEventListener('change', e => {
    const errorDiv = document.getElementById('card-errors')
    if (e.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${e.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

const form = document.getElementById('payment-form');

form.addEventListener('submit', e => {
    e.preventDefault();
    card.update({
        'disabled': true
    })
    $('#submit-button').attr('disabled', true)

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(result => {
        const errorDiv = document.getElementById('card-errors')
        if (result.error) {
            card.update({
                'disabled': false
            })
            $('#submit-button').attr('disabled', false)
            const html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});