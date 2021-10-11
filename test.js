var utherThis = new SpeechSynthesisUtterance("Teste voz um dois três");
var synth = window.speechSynthesis;

voices = synth.getVoices();
utherThis.voice = voices[1] // 0 - daniel, 1 - maria, default: daniel
synth.speak(utherThis);

// calendario html
// lista de tarefas
// 