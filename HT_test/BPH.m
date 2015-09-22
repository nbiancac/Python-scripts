clear all
close all

cd('/afs/cern.ch/user/n/nbiancac/scratch0/HEADTAIL_RELEASE/Store/Model_perturbated')
filesToreadpert=dir('BPV.*.dat');

cd('/afs/cern.ch/user/n/nbiancac/scratch0/HEADTAIL_RELEASE/Store/Model_unperturbated')
filesToreadunpert=dir('BPV.*.dat');

for kk=1:length(filesToreadpert)
cd('/afs/cern.ch/user/n/nbiancac/scratch0/HEADTAIL_RELEASE/Store/Model_perturbated')
datatmppert=dlmread(filesToreadpert(kk).name);
disp(kk)
FFT=fft(datatmppert(:,2));
ABS=abs(FFT);
PH=phase(FFT)*180/pi;

[nicolo,indtmp]=max(ABS);
phpert(kk)=PH(indtmp);


cd('/afs/cern.ch/user/n/nbiancac/scratch0/HEADTAIL_RELEASE/Store/Model_unperturbated')
datatmpunpert=dlmread(filesToreadunpert(kk).name);
disp(kk)
FFT=fft(datatmpunpert(:,2));
ABS=abs(FFT);
PH=phase(FFT)*180/pi;

[nicolo,indtmp]=max(ABS);
phunpert(kk)=PH(indtmp);


%figure(1)
%plot([1:size(pertfft,1)],pertfft)
%hold on
%plot([1:size(unpertfft,1)],unpertfft,'r')
%hold off

end

