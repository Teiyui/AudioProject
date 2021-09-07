
cd C:\Users\admin\Desktop

echo "playing audio"

for %%i in (1 2 3 4 5 6) do (

sox "mytestspeech.wav" -t waveaudio

time /t

timeout /t 6 /nobreak

)
