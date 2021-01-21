# 테라 클래식 소탕 매크로 설명서
> Python 모듈로 간단하게 구현.


 * 테라 클래식이라는 모바일게임에서 "소탕 퀘스트"를 자동으로 진행하고 싶어서 매크로를 제작  
 * 커스텀 하려면 Python 3.7.4, pyautogui 설치가 필요 (다른 버전은 테스트 해 보지 않음)     
 

 ## 1. 시작 전 에뮬레이터 세팅 
 
 
 * 사용 에뮬레이터 :  
     * LDPlayer
 
 * 해상도 :  
     * 1280 x 720 (dpi 240)
     * 다른 해상도는 아직 미구현  
      
 * 인게임 설정:  
     * 그래픽 옵션 최하
     * 프레임 제한 25
 
  
  

 ## 2. '.exe' 파일을 실행 시키는 방법  
 * 주의! - LFS를 사용한 '.exe' 파일이기 때문에 저장소를 clone해야 정상 작동 한다.  
 
 ![화면2](https://user-images.githubusercontent.com/46941349/63182647-ff709200-c08d-11e9-82a6-7755fc70dc25.PNG)  
 1. 소탕 환경, 가방 비우기를 설정한다.  
 2. macro.exe 파일과 data폴더를 같은 경로에 두고 시작한다.  
    ex) 바탕화면에 매크로 폴더를 만든 뒤 macro.exe 파일과 data폴더 를 넣어준다.  
 3. 소탕 버튼이 보이게 두고 macro.exe 실행 후 '시작' 버튼을 누른다.  
    * 항상 윈도우 최상위에 LDPlay가 실행되고 있어야 동작한다. 따라서 자는시간에 이용한다  
 
 * ~~사용하는 모듈이 pyinstaller, py2ex 등에서 변환이 안된다.. 왜일까..ㅜ~~  
 * 해결했다!
 
 ## 3. Python 언어를 사용해서 구동 및 커스텀을 하기위한 개발환경 설명  
 ### Python 설치하기  
 Python 설치는 공식 [홈페이지](https://www.python.org/) 참고  
 ### pyautogui 설치하기  
```sh
pip install pyautigui
```
 ### tkinter 설치하기  
 간혹 Python은 설치되어있는데 tkinter가 설치되어있지 않은 경우가 있다.  
 ```sh
 pip install tkinter
 ```
 ### 구동 및 커스텀 하기  
 * data 폴더와 macro.py를 같은 경로에 위치시키고 코드를 실행한다.  
 * [요기](https://github.com/Sungmin-Joo/Codes_for_Beginners/tree/master/Python) + 킹갓 Google을 이용하여 Python을 공부해서 커스텀을 하면 된다.
 
 ## 업데이트 내역
 * v1.0 - 엄청 간단하게 버튼을 찾아서 눌러준다. (버전이라 표기하기도 민망하다) - 19/08/15
 * 1280 x 720 (dpi 240) 보다 더 낮은 해상도에서도 구동 가능하다. - 19/08/18
 * 게임에 너무 많은 시간이 들어갈 것 같아서 그만두었다. 다른걸 열심히 할 예정이다. - 19/08/20  
 
 
 ## Info
 Name      : 주성민(Joo Sung Min)  
 E-mail    : big-joo_dev@naver.com  
 Phone     : 010-2770-4367
 Univesity : Korea Polytechnic University  
 
 버그가 있다면 제보를 부탁 드립니다.  
   
  BSD 3-Clause License 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.

 [LICENSE](https://github.com/Sungmin-Joo/TERA_macro/blob/master/LICENSE)
 
 *(오픈소스 라이센스 관련 지식이 부족하여 모듈에 적용되는 라이센스들이 호환되도록 유지함)
