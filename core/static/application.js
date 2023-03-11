//! varible declaration
var search_product_uuid = document.getElementById("search_product_uuid");
var search_product_by_name = document.getElementById("search_product_by_name");
const crf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const resultsBox = document.getElementById("results-box");
const product__table = document.getElementById("product__table");
const delete_product_btn = document.getElementById("delete_product_btn");
console.log(crf);

const send_search_product = async (product) => {
  $.ajax({
    type: "POST",
    url: "/product_search",
    data: {
      csrfmiddlewaretoken: crf,
      product: product,
    },
    success: (response) => {
      if (Array.isArray(response.data)) {
        resultsBox.innerHTML = "";
        response.data.forEach((product) => {
          resultsBox.innerHTML += `<a href="" class="list-group-item list-group-item-action" onclick="send_search_product_uuid_from_popup('${product.code}')">
          <div class="d-flex  mt-2 mb-2">
          
            <div class="mr-2">
                <h5 class="product-name">${product.code}</h5>

            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.name}</h5>
               
            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.price}</h5>
               
            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.description}</h5>
               
            </div>

          </div>
          </a>`;
        });
      } else {
        if (searchInput.value.length > 0) {
          resultsBox.innerHTML = `<b>${response.data}</b>`;
        } else {
          resultsBox.innerHTML = "";
        }
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

// ! PRODUCT SEARCH INPUT keyup event
search_product_by_name.addEventListener("keyup", function (event) {
  console.log(event.target.value);

  if (event.target.value.length > 0) {
    send_search_product(event.target.value);
  } else {
    resultsBox.innerHTML = "";
  }
});

//! update the product table
function update_product_table() {
  // Get the cart items from local storage
  const cart = JSON.parse(localStorage.getItem("cart")) || {};

  // Clear the table contents
  product__table.innerHTML = "";
  console.log("update product table");
  console.log(cart);
  // Loop through each item in the cart and add it to the table
  for (const product_uuid in cart) {
    const product = cart[product_uuid];
    // ! Show the product table
    const product_table = document.getElementById("product__table");
    //  create table header
    const product_table_header = document.createElement("thead");
    product_table_header.innerHTML = `<thead>
    <tr>
      <th scope="col">Product Name</th>
      <th scope="col">Quantity</th>
      <th scope="col">Price</th>
      <th scope="col">Total Price</th>
      <th scope="col">Discount</th>
      <th scope="col">Action</th>

    </tr>
  </thead>
  `;
    // ! create a row for the product
    const product_row = document.createElement("tr");

    // const product__table_body = document.getElementById('product__table_body')
    // console.log(product__table_body)
    // //! create a row for the product
    // var product_row = document.createElement("tr");
    // // product_row.innerHTML = ` <td>${count}</td>`;
    product_row.innerHTML += ` <td>${product.product_name}</td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.quantity}" id="product_quantity_input" class="form-control" placeholder="Enter the quantity" /> </td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.sales_price}" id="product_price_input" class="form-control" placeholder="Enter the price" disabled /> </td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.total_price}" id="product_total_price_input" class="form-control" placeholder="Enter the price" disabled /> </td>`;
    product_row.innerHTML += ` <td>  <input type="text" value="${product.discount}" onblur="update_product_price('${product_uuid}')" id=${product_uuid} class="form-control" placeholder="Enter the discount" /> </td>`;
    product_row.innerHTML += ` <td> <button class="btn btn-danger" id="delete_product_btn" onclick="delete_product('${product_uuid}')">Delete</button> </td>`;

    /// include the table header once
    if (product_table.childElementCount == 0) {
      product_table.appendChild(product_table_header);
    }
    product_table.appendChild(product_row);
  }
}

//? querying for products
const send_search_product_uuid = async (product) => {
  console.log(product);
  $.ajax({
    type: "GET",
    url: `/get_product_by_uuid/${product}`,
    success: (response) => {
      if (response) {
        const product_name = response.product_name;
        const sales_price = response.sales_price;
        const quantity = 1;
        const product_uuid = response.product_uuid;
        const product = {
          product_name,
          sales_price,
          quantity,
          product_uuid,
        };
        console.log(product);
        // If the product exists, increment its quantity in the cart
        const cart = JSON.parse(localStorage.getItem("cart")) || {};
        if (cart[response.product_uuid]) {
          cart[response.product_uuid].quantity++;
          cart[response.product_uuid].total_price =
            cart[response.product_uuid].quantity *
            cart[response.product_uuid].sales_price;
        } else {
          cart[response.product_uuid] = {
            product_name: response.product_name,
            sales_price: response.sales_price,
            old_price: response.sales_price,
            quantity: 1,
            product_uuid: response.product_uuid,
            total_price: response.sales_price * 1,
            discount: 0,
          };
        }
        localStorage.setItem("cart", JSON.stringify(cart));
      } else {
        // If the product doesn't exist, show an error message
        alert("Product not found");
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

function send_search_product_uuid_from_popup(product) {
  // prevent default form submission

  e = window.event;
  e.preventDefault();

  console.log(product);
  $.ajax({
    type: "GET",
    url: `/get_product_by_uuid/${product}`,
    success: (response) => {
      if (response) {
        const product_name = response.product_name;
        const sales_price = response.sales_price;
        const quantity = 1;
        const product_uuid = response.product_uuid;
        const product = {
          product_name,
          sales_price,
          quantity,
          product_uuid,
        };
        console.log(product);
        // If the product exists, increment its quantity in the cart
        const cart = JSON.parse(localStorage.getItem("cart")) || {};
        if (cart[response.product_uuid]) {
          cart[response.product_uuid].quantity++;
          cart[response.product_uuid].total_price =
            cart[response.product_uuid].quantity *
            cart[response.product_uuid].sales_price;
        } else {
          cart[response.product_uuid] = {
            product_name: response.product_name,
            sales_price: response.sales_price,
            old_price: response.sales_price,
            quantity: 1,
            product_uuid: response.product_uuid,
            total_price: response.sales_price * 1,
            discount: 0,
          };
        }
        localStorage.setItem("cart", JSON.stringify(cart));
      } else {
        // If the product doesn't exist, show an error message
        alert("Product not found");
      }
    },
    error: (error) => {
      console.log(error);
    },
  });

  const product_popup_search = document.getElementById("product_popup_search");

  

  // <div class="modal fade bd-example-modal-lg show" tabindex="-1" id="product_popup_search" style="display: block;" aria-modal="true" role="dialog">

  // product_popup_search.style.visibility = "hidden";

  update_product_table();
}

search_product_uuid.addEventListener("keyup", function (event) {
  event.preventDefault();
  if (event.key === "Enter") {
    console.log(event.target.value);
    send_search_product_uuid(event.target.value);
    search_product_uuid.value = "";
    update_product_table();
  }
  //! set search_product_uuid empty and focus in it
  search_product_uuid.focus;

  // if (event.target.value.length  >= 12) {
  //   //! set search_product_uuid empty and focus in it
  //   send_search_product_uuid(event.target.value);

  //   search_product_uuid.value = "";
  // }
});

document.addEventListener("keydown", function (event) {
  if (event.altKey) {
    document.getElementById("searh_modal_popup").click();
  }
});

console.log("Hello World");

//? Hide the product popup
document.getElementById("close_product_popup").onclick = function () {
  document.getElementById("product_popup").style.display = "none";
  document.getElementById("product_popup").style.visibility = "hidden";
};

function delete_product(product_uuid) {
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  delete cart[product_uuid];
  localStorage.setItem("cart", JSON.stringify(cart));
  update_product_table();
}

function update_product_price(product_uuid) {
  e = window.event;
  e.preventDefault();
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  // geting the specific product row from the cart
  const product_price_discount = document.getElementById(product_uuid).value;

  // check if it is a number
  if (isNaN(product_price_discount)) {
    alert("Please enter a valid number");
  } else {
    cart[product_uuid].discount = product_price_discount;

    // if discount is  is zero then set the sales price to the old price
    if (product_price_discount == 0) {
      cart[product_uuid].sales_price = cart[product_uuid].old_price;
      cart[product_uuid].total_price =
        cart[product_uuid].quantity * cart[product_uuid].sales_price;

      console.log(cart[product_uuid].total_price);
      // set the current total price to the new total price
      const product_total_price_input = document.getElementById(
        "product_total_price_input"
      );
      product_total_price_input.value = cart[product_uuid].total_price;
      localStorage.setItem("cart", JSON.stringify(cart));
      update_product_table();
    } else {
      cart[product_uuid].sales_price =
        cart[product_uuid].sales_price - product_price_discount;
      cart[product_uuid].total_price =
        cart[product_uuid].quantity * cart[product_uuid].sales_price;
      // set the current total price to the new total price
      const product_total_price_input = document.getElementById(
        "product_total_price_input"
      );
      product_total_price_input.value = cart[product_uuid].total_price;

      localStorage.setItem("cart", JSON.stringify(cart));
      update_product_table();
    }
  }
}
