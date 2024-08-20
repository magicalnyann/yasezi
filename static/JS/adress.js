function searchAddress() {
    new daum.Postcode({
        oncomplete: function(data) {

            var addressField = document.getElementById("address");
            var addressDetailField = document.getElementById("address_detail");

            addressField.value = data.address;

            addressDetailField.value = data.bname;
        }
    }).open();
}
