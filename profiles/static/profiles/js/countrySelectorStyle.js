const country_input = document.getElementById('id_default_country');
const setInputColor = e => {
    if (country_input.value != '') {
        country_input.style.color = '#495057';
    } else {
        country_input.style.color = '#aab7c4';
    }
};

document.addEventListener('DOMContentLoaded', setInputColor);
country_input.addEventListener('change', setInputColor);