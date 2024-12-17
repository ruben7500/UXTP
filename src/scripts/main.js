
async function fetchProducts(page = 1) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/products?page=${page}`);
        const products = await response.json();
        const productList = document.getElementById('product-list');

        products.forEach(product => {
            const productCard = `
                <div class="bg-white p-4 shadow rounded">
                    <h2 class="text-xl font-semibold">${product.name}</h2>
                    <p class="text-gray-700">${product.description}</p>
                    <p class="text-blue-500 font-bold">$${product.price}</p>
                </div>
            `;
            productList.innerHTML += productCard;
        });
    } catch (error) {
        console.error("Error fetching products:", error);
    }
}


let currentPage = 1;

// Infinite scroll implementation
window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        currentPage++;
        fetchProducts(currentPage);
    }
});

fetchProducts();
