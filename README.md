## Rasberry_pie

----------------

This is an detect module created during the second semester of 23.
I am using various parts, and I wrote it using python.

23년도 2학기, 마이크로 프로세서 프로젝트에 작성하였습니다.
파이썬으로 작성한 알람시계 모듈 스크립트이며 4개의 버튼을 사용합니다.

master분기에 코드가 있습니다.

----------------

moudle : detectTrace
>피에조 부저, 카메라, 움직임 감지 센서, 초음파 센서를 활용하여 접근하는 무언가의 detect를 탐지하고, 그를 로그로 출력합니다.
>여기서, detect된 무언가가 주위에 있는 물체일 수 있으니, 움직임 감지 센서로 장치에 접근하려는 시도가 있는지 파악하고, 시도가 있다면 카메라로 촬영을 진행합니다.
>지속적으로 감지가 된다면, n초 이후에 카메라를 다시 사용하여 촬영을 시작합니다.
>이 모든 과정은 로그로 출력이 됩니다.
