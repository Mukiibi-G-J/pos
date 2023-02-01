//! varible declaration
var search_product_uuid = document.getElementById("search_product_uuid");

//! querying for products
function send_search_product_uuid(product_uuid) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", `/get_product_by_uuid/${product_uuid}`, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ product_uuid: product_uuid }));
  console.log(xhr);
  //get the response from the server
  xhr.onload = function () {
    //! append the products to a list of products
    var product_list = [];
    var product = JSON.parse(xhr.response);
    product_list.push(product);

    //! loop through the list for each product
    var count = 0;
    product_list.forEach((product, index) => {
      // ! Show the product table
      document.getElementById("product__table").style.display = "block";
      //! get the product table
      var product__table_body = document.getElementById("product__table_body");
      //! create a table row for each product in the list
      var product_row = document.createElement("tr");
      //! check if the product is in the list
      if (product.product_uuid === product.product_uuid) {
        //! if the product is in the list increment the quantity
        var quantity = quantity++;
        product_row.innerHTML = ` <td>${count}</td>`;
        product_row.innerHTML = ` <td>${product.product_uuid}</td>`;
        product_row.innerHTML += ` <td>${product.product_name}</td>`;
        product_row.innerHTML += ` <td> <input type="number" value="${quantity}" id="product_quantity_input" class="form-control" placeholder="Enter the quantity" /> </td>`;
      } else {
        product_row.innerHTML = ` <td>${count}</td>`;
        product_row.innerHTML = ` <td>${product.product_uuid}</td>`;
        product_row.innerHTML += ` <td>${product.product_name}</td>`;
        product_row.innerHTML += ` <td> <input type="number" value="" id="product_quantity_input" class="form-control" placeholder="Enter the quantity" /> </td>`;
        product_row.innerHTML += ` <td> <input type="number" value="${product.sales_price}" id="product_price_input" class="form-control" placeholder="Enter the price" /> </td>`;
        // product_row.innerHTML += ` <td>
        // <input type="number" value="${product.sales_price}" id="product_price_input" class="form-control" placeholder="Enter the price" />
        // </td>`;
      }

      product__table_body.appendChild(product_row);
      //! increment the count
      count++;
      // store count
      // localStorage.setItem("count", count);
    });

    // ! Fill the product table
    // document.getElementById("product_uuid").innerHTML = product.product_uuid;
    // document.getElementById("product_price").innerHTML = `
    //
    // document.getElementById("product_quantity").innerHTML = product.quantity;
    // document.getElementById("product_popup_description").innerHTML =
    //   product.description;
    // document.getElementById("product_popup_image").src = product.image;
  };
}
search_product_uuid.addEventListener("keyup", function (event) {
  if (event.target.value.length === 14) {
    //! set search_product_uuid empty and focus in it
    send_search_product_uuid(event.target.value);

    search_product_uuid.value = "";
  }
});

document.addEventListener("keydown", function (event) {
  if (event.altKey) {
    document.getElementById("searh_modal_popup").click();
  }
});

console.log("Hello World");

//! Hide the product popup
document.getElementById("close_product_popup").onclick = function () {
  document.getElementById("product_popup").style.display = "none";
  document.getElementById("product_popup").style.visibility = "hidden";
};

// document.getElementById("search_product_uuid").onkeyup = function() {

//   var product_uuid = document.getElementById("search_product_uuid").value;
//   console.log(product_uuid);
//   console.log("product_uuid")

// ! Ajax request
// var xhr = new XMLHttpRequest();
// xhr.open("GET", "/get_product_by_uuid", true);
// xhr.setRequestHeader("Content-Type", "application/json");
// xhr.send(JSON.stringify({ product_uuid: product_uuid }));
// console.log(xhr);
// }
