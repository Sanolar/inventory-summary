// Load inventory on page load
window.onload = fetchInventory;

document.getElementById("updateForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const quantity = parseInt(document.getElementById("quantity").value);
    const price = parseFloat(document.getElementById("price").value);

    await fetch("/inventory-summary/update", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, quantity, price })
    });
    fetchInventory();
});

document.getElementById("saleForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("saleName").value;
    const quantity = parseInt(document.getElementById("saleQty").value);

    const response = await fetch("/inventory-summary/sale", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items: [{ name, quantity }] })
    });
    const result = await response.json();
    document.getElementById("billOutput").innerText = `Sale Total: $${result.total_sale}`;
    fetchInventory();
});

async function fetchInventory() {
    const res = await fetch("/inventory-summary/");
    const data = await res.json();
    const tbody = document.querySelector("#inventoryTable tbody");
    tbody.innerHTML = "";
    data.forEach(item => {
        const row = `<tr>
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>$${item.price.toFixed(2)}</td>
        </tr>`;
        tbody.innerHTML += row;
    });
}
