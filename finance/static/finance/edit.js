
document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#editbtn').style.display = "block";
    document.querySelector('#savebtn').style.display = "none";

    document.querySelector("#editbtn").addEventListener('click', (event) => {
        edit(event);
    });

});

function edit(event){
    event.preventDefault();
    var percentages =  document.querySelectorAll(".percent");
    var ori_values = [];

    for (let i= 0; i < 5; i++) {
        content = percentages[i].innerHTML;

        percentages[i].innerHTML = `<textarea class="newcontent" data-id="${i}">${content}</textarea>`;
    }

    document.querySelector('#editbtn').style.display = "none";
    document.querySelector('#savebtn').style.display = "block";

    document.querySelector("#savebtn").addEventListener('click', () => {
        for (let i= 0; i < 5; i++) {
            ori_values.push(document.querySelector(`.newcontent[data-id="${i}"]`).value);
        }
        save_percentages(ori_values);
    });


}

function save_percentages(ori_values){
    console.log(ori_values);

    form = new FormData();
    form.append("tax", ori_values[0]);
    form.append("emergency", ori_values[1]);
    form.append("insurance", ori_values[2]);
    form.append("pension", ori_values[3]);
    form.append("spending", ori_values[4]);

    fetch("/edit", {
        method: "POST",
        body: form
    })
    .then((response)=>{
        console.log(response);
        location.reload();
    })
    .catch(error =>{
        console.log('Error:', error);
    });

    
}