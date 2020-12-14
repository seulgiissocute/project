# 무선네트워크 프로젝트

## 팀원
- 경규영, 박선우, 이슬기, 정승원

## 아이디어

  - 스마트 화분

    - 개요 : 자신만의 화분을 관리하고, 화분에 대해 신경을 자주 쓰지 못하는 바쁜 현대인들의 니즈를 충족시키기 위한 스마트 화분을 개발할 필요성이 있음
  
    - 개발 목적 : 라즈베리파이와 토양수분센서를 이용하여 토양의 상태 확인 및 자동 수분 공급
  
    - 사용된 부품
      - 토양수분센서
      - 워터펌프
      - 모터드라이브
      - ADC모듈
      - LED
      - 미니브레드보드
      - 수조, 고무호스, 화분
     
     
     - 서비스
  
       1. 토양 수분 상태 확인
    
          - 토양의 수분 측정 : 라즈베리파이와 토양수분센서 이용
      
          - 토양의 수분 상태에 따른 LED 점등 및 소등으로 시각적 표현
      
          - 실시간으로 화분에 있는 토양의 상태를 확인하여, 임계치 미달일 경우 LED 점등
    
    
    
        2. 자동 수분 공급 기능
    
            - 자동 수분 공급 : 워터펌프 이용
       
            - 실시간으로 화분에 있는 토양의 습도를 확인하여, 임계치 미달일 경우 자동으로 화분에 수분을 공급
      
      
      
        3. 메시지 기능
    
            - 메시지 : 라즈베리파이와 텔레그램 이용
      
            - 텔레그램을 통하여 사용자 편의를 제공
      
            - 수분 공급 기능의 장비 이상 유무를 확인 할 수 있도록, 임계치 도달 및 워터펌프가 중단 시 메시지 전송
      
      
      

  ### 시스템 구조
  - 시스템 구성도
      ![structure](https://user-images.githubusercontent.com/71371940/101891035-dcec7b80-3be4-11eb-9c4b-831a60f7b424.png)


  - 순서도  
      ![flowchart2](https://user-images.githubusercontent.com/71371940/102121450-560afd80-3e87-11eb-8fd9-197582e001b7.JPG)
