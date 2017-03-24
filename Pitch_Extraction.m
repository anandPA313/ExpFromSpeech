%Pitch Extraction;
[y,Fs]=audioread('C:\Users\Hitesh S\Downloads\Documents\Sample.wav');
%To get a 20ms time window I'll do 1/Fs and then 20ms*1/Fs;
Ts=1/Fs;
No_of_Samples_20ms=20e-3/Ts;
%I'll do 20ms timeframe then shift by 10ms to the right and repeat;
Sample_Shift=10e-3/Ts;
for j=0:Sample_Shift:length(y)-No_of_Samples_20ms
    
    Samples_20ms=(y(1+j:No_of_Samples_20ms+j,1))'; 
    [AutoCorr,delay]=xcorr(Samples_20ms,Samples_20ms);
    figure,plot(delay,abs(AutoCorr));
    [LMax,IndexMax]=findpeaks(abs(AutoCorr));
    Max=max(LMax);
    Max2=0;
    for i=1:length(IndexMax)
        if ( LMax(i)>Max2 && LMax(i)<Max )
            Max2=LMax(i);
            Index=IndexMax(i);
        end
    end
    Time_Delay_Pitch=abs(delay(Index))*Ts;
    disp(1/Time_Delay_Pitch);
end