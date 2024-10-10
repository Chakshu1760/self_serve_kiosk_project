const menuItems = {{ menu|tojson }};

function showItems(category) {
    console.log(`Showing items for category: ${category}`); // Debugging line
    const filteredItems = menuItems.filter(item => item.category === category);
    const menuDiv = document.getElementById('menu');
    menuDiv.innerHTML = ''; // Clear previous items

    filteredItems.forEach(item => {
        menuDiv.innerHTML += `<div class="menu-item">
            <button class="item-button" value='{"item": "${item.item}", "price": ${item.price}}'>
                ${item.item}: $${item.price}
            </button>
        </div>`;
    });
}

function placeOrder() {
    const selectedItems = Array.from(document.querySelectorAll('input[type="checkbox"]:checked')).map(input => JSON.parse(input.value));
    fetch('/order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ items: selectedItems })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('total').innerText = `Total: $${data.total.toFixed(2)}`;
    });
}
