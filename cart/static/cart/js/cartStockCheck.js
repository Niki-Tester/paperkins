const qtyInputs = document.getElementsByClassName('qty-input')
const checkoutButton = document.getElementById('checkout-button')
const orderLimitMessage = document.getElementById('order-limit-message')
const itemQtyData = {}

for (const input of qtyInputs) {
    const itemId = input.dataset.itemId
    const qty = parseInt(input.value)
    const max = input.max
    if (itemQtyData.hasOwnProperty(itemId)) {
        itemQtyData[itemId] = {
            'orderQty': itemQtyData[itemId]['orderQty'] + qty,
            'max': max
        }
    } else {
        itemQtyData[itemId] = {
            'orderQty': qty,
            'max': max
        }
    }
}

for (const itemId in itemQtyData) {
    if (Object.hasOwnProperty.call(itemQtyData, itemId)) {
        const item = itemQtyData[itemId];
        if (item['orderQty'] > item['max']) {
            checkoutButton.title = 'Order limit exceeded on one or more cart items. Please reduce quantities and update cart.'
            orderLimitMessage.innerText = 'Order limit exceeded on one or more cart items. Please reduce quantity and update cart.'
            checkoutButton.addEventListener('click', e => {
                e.preventDefault()
            })
            for (const input of qtyInputs) {
                if (input.dataset.itemId === itemId) {
                    input.style.backgroundColor = '#fbb'
                }
            }
            checkoutButton.style.cursor = 'not-allowed';
        }
    }
}