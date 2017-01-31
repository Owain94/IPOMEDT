function shutDown() {
    swal({
        title: "Are you sure you want to shutdown?",
        text: "This proccess can't be undone",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, shutdown!",
        cancelButtonText: "No, cancel shutdown!",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            swal("Success!", "The server has been shutdown.", "success");
            var url = "/shutdown.html";
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open("GET", url, false);
            xmlHttp.send(null);
            return xmlHttp.responseText;
        } else {
            swal("Cancelled", "Your shutdown action is cancelled", "error");
        }
    });
}

function reboot() {
    swal({
        title: "Are you sure you want to reboot?",
        text: "This proccess can't be undone",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, reboot!",
        cancelButtonText: "No, cancel reboot!",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            swal("Success!", "The server has been rebooted.", "success");
            var url = "/reboot.html";
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open("GET", url, false);
            xmlHttp.send(null);
            return xmlHttp.responseText;
        } else {
            swal("Cancelled", "Your reboot action is cancelled", "error");
        }
    });
}

function start() {
    var url = "/start.html";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function headlightsOn() {
    var url = "/headlights_on.html";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function headlightsOff() {
    var url = "/headlights_off.html";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function sireneOn() {
    var url = "/sirene_on.html";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function sireneOff() {
    var url = "/sirene_off.html";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function setData() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/log.html", true);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            var dataArray = xhr.responseText;
            dataArray = dataArray.split("\n");

            $("#consoleText").html(dataArray.join("<br />")).scrollTop($("#consoleText")[0].scrollHeight);
        }
    };
    xhr.send(null);
}

setInterval(function() {
    setData();
}, 1000);

document.getElementById("shutdown").addEventListener("click", shutDown);
document.getElementById("reboot").addEventListener("click", reboot);
document.getElementById("start").addEventListener("click", start);
document.getElementById("headlights_on").addEventListener("click", headlightsOn);
document.getElementById("headlights_off").addEventListener("click", headlightsOff);
document.getElementById("sirene_on").addEventListener("click", sireneOn);
document.getElementById("sirene_off").addEventListener("click", sireneOff);