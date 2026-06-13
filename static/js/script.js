const socket = io();
let vid = document.getElementById("video");
function getPerm(){
    vid.play();

};
socket.on("update", (data) => {
    if(data === "on"){
        document.getElementById('IntroPara').innerHTML = "<strong>Gesture Registered Successfully (⌐■_■)</strong>";
        vid.play();
    };
     if(data === "off"){
        document.getElementById('IntroPara').innerHTML = "<p>Gesture Not Detected (￣o￣) . z Z</p>";
    };
});
