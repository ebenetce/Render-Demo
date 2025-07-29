FROM mathworks/matlab-deps:R2025a

RUN apt-get update && apt-get upgrade -y && apt-get install wget -y

ENV EXTRACTEDDIR="/opt/matlabruntime/unzippedinstaller"

RUN mkdir -p $EXTRACTEDDIR && wget https://ssd.mathworks.com/supportfiles/downloads/R2025a/Release/1/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_R2025a_Update_1_glnxa64.zip && unzip MATLAB_Runtime_R2025a_Update_1_glnxa64.zip -d $EXTRACTEDDIR   

WORKDIR $EXTRACTEDDIR

# Write the installer file
RUN touch ./installInputs.txt
RUN printf "destinationFolder=/tmp/matlabruntime/runtime\nagreeToLicense=yes\n" > ./installInputs.txt
RUN printf "product.MATLAB Base Runtime\n" >> ./installInputs.txt
RUN printf "product.MATLAB Production Server Runtime Addon\n" >> ./installInputs.txt

# Run the installer
RUN ./install -bat true -inputFile ./installInputs.txt

ENV TZ="Etc/UTC"

RUN unlink /opt/matlabruntime/R2025a/sys/os/glnxa64/libstdc++.so.6
RUN ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /opt/matlabruntime/R2025a/sys/os/glnxa64/libstdc++.so.6

ENV LD_LIBRARY_PATH="/opt/matlabruntime/R2025a/runtime/glnxa64:/opt/matlabruntime/R2025a/bin/glnxa64:/opt/matlabruntime/R2025a/sys/os/glnxa64:/opt/matlabruntime/R2025a/sys/opengl/lib/glnxa64:/opt/matlabruntime/R2025a/extern/bin/glnxa64"

RUN apt-get update && apt-get upgrade -y

COPY service1/applicationFilesForMATLABCompiler /usr/bin/mlrtapp
RUN chmod -R a+rX /usr/bin/mlrtapp/*

RUN if ["$(getent passwd appuser | cut -d: -f1)" = ""] ; then useradd -ms /bin/bash appuser ; fi
USER appuser

ENTRYPOINT ["/opt/matlabruntime/R2025a/bin/glnxa64/muserve", "-a", "/usr/bin/mlrtapp/mymagic.ctf"]