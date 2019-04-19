import os
import sys
import time

print(f"환영합니다, {os.getlogin()} 님\n")
time.sleep(2)
print("이 프로그램은 pip가 path에 등록되지 않아 명령 프롬포트에서 \
pip install을 사용할 수 없는 파린이들을 대상으로 제작되었습니다.\n")
time.sleep(1)
print("주의! import 시 바로 작동되는 모듈의 경우 중간에 프로그램이 멈출 수 있습니다.\n \
허나 그 경우 모듈 자체는 정상적으로 다운받아진 것이니 강제 종료하셔도 무방합니다.\n")

version = str(sys.version_info.major)+str(sys.version_info.minor)
bitLocation = sys.version.find("bit")
bit = str(sys.version[bitLocation-3])+str(sys.version[bitLocation-2])
pipPath = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python{version}-{bit}\\Scripts'

def start():
  print("INSTALL 하실 MODULE NAME을 입력해주세요.")
  M_name = input(":")
  launch(M_name)
  re = input("추가로 더 다운받을 모듈이 있습니까?\n있으면 y를 눌러주세요.")
  if re in ['y', "Y", "ㅛ"]:
    start()
  else:
    print("사용해주셔셔 감사합니다.")
    time.sleep(3)

def launch(M_name, count=0):
  try:
    print("모듈 설치 여부를 확인합니다.")
    time.sleep(3)
    setattr(sys.modules[__name__], M_name, __import__(M_name, fromlist=[M_name]))
  except ModuleNotFoundError:
    count += 1
    print("모듈이 존재하지 않습니다.")
    time.sleep(2)
    print("다운로드를 시작합니다.")
    if count > 1:
      print("해당 모듈이 존재하지 않거나, 모종의 이유로 모듈을 설치할 수 없습니다.\n\
            프로그램을 종료합니다.")
      quit()
    os.chdir(pipPath)
    os.system(f"pip.exe install {M_name}")
    time.sleep(2)
    input("설치가 완료되었다면 확인을 위해 엔터 키를 눌러주세요.")
    launch(M_name, count)
  else:
    time.sleep(3)
    print("\n모듈이 확인되었습니다.\n")
  
if __name__ == "__main__":
  start()
