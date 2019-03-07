function myFriend() {
    alert("The second one");
}

function myFunction() {
    alert("Hello");
}

function addSecondDownloadAddress(addresses){
    var obj = JSON.parse(addresses)
    var node = document.createElement('div');
    var content = "";
    //node.innerHTML=
    //'<div class="form-group"><label class="col-sm-2 control-label">Select second download address</label><div class="dropdown col-sm-10"><div class="form-group"><select class="form-control" id="download2">{% for address in addresses %}<option>{{address.street}} {{address.city}}</option>{% endfor %}</select></div></div></div>'
    content='<div class="form-group"><label class="col-sm-2 control-label">Select second download address</label><div class="dropdown col-sm-10"><div class="form-group"><select class="form-control" id="download2">'
    for (j in obj){
        content += "<option "
        content += "value=\"" + obj[j].pk+"\">"
        content += obj[j].fields.street + " " + obj[j].fields.city
        content += "</option>"
    }


//    Object.keys(addresses).forEach(function(key){
////        var node = document.createElement('option');
//        alert(key)
////        alert(addresses['fields'])
////        node.innerHTML+="<option>"
////        node.innerHTML+=addresses[key]['street'] + " " + addresses[key]['city']
////        node.innerHTML+="</option>"
//    })
    content += '</select></div></div></div>'
    node.innerHTML = content
    document.getElementById("secondAddress").appendChild(node)
}