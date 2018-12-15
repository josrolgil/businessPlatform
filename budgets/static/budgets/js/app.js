function myFriend() {
    alert("The second one");
}

function myFunction() {
    alert("Hello");
}

function addSecondDownloadAddress(addresses){
    var node = document.createElement('div');
    //node.innerHTML=
    //'<div class="form-group"><label class="col-sm-2 control-label">Select second download address</label><div class="dropdown col-sm-10"><div class="form-group"><select class="form-control" id="download2">{% for address in addresses %}<option>{{address.street}} {{address.city}}</option>{% endfor %}</select></div></div></div>'
    node.innerHTML='<div class="form-group"><label class="col-sm-2 control-label">Select second download address</label><div class="dropdown col-sm-10"><div class="form-group"><select class="form-control" id="download2">'

//    Object.keys(addresses).forEach(function(key){
//        var node = document.createElement('option');
//        alert(addresses['fields'])
//        node.innerHTML+="<option>"
//        node.innerHTML+=addresses[key]['street'] + " " + addresses[key]['city']
//        node.innerHTML+="</option>"
//    })
    alert(addresses)
    json.forEach(function(obj['fields']){
        alert(obj)

    })
    node.innerHTML+='</select></div></div></div>'
    document.getElementById("secondAddress").appendChild(node)
}