## 1. What is this project?
이 프로젝트는 llama2 7b Q4모델을 사용하여 local환경에서 직접 구동하기 위해 제작한 프로젝트 이다.
html과 js 그리고 flask를 사용하여 GUI환경을 구성하였다.

## 2. How powerful should your computer be? <br> (computer specifications)

<table>
  <tr>
    <th>
        <b>최소 사양</b><br>
        window의 경우<br>
        CPU: intel I5 12700f<br>
        RAM: 16GB<br>
        GPU: rtx3060 8GB<br>
        SSD: 32GB<br>
        <br>
        MAC의 경우 macbook m2 air<br>
    </th>
    <th>
        <b>권장사양</b><br>
        window의 경우<br>
        CPU: intel I7 12700KF<br>
        RAM: 24GB<br>
        GPU: rtx3060 16GB<br>
        SSD: 64GB<br>
        <br>
        MAC의 경우 macbook m1pro<br>
    </th>
  </tr>
</table>

나의 경우 m1pro 기본 모델을 사용

## 3. How to use
*경고:* 해당 코드는 venv가상환경에서 사용하는것을 추천합니다.

가상환경 제작  
`python3 -m venv venv`

<table>
  <tr>
    <th>
    [macOS / Linux]<br>
    <pre><code>source venv/bin/activate</code></pre>
    </th>
    <th>
    [Windows CMD]
    <pre><code>venv\Scripts\activate</code></pre>
    </th>
    <th>
    [Windows PowerShell]
    <pre><code>venv\Scripts\Activate.ps1</code></pre>
    </th>
  </tr>
</table>

필요한 모듈 install 하기  
`pip install -r requirements.txt`

llama.cpp 저장소 클론  
`git clone https://github.com/ggerganov/llama.cpp`

모델 저장소 생성  
`mkdir models`

mac OS brew에서 cmake사용
```
brew install cmake
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

모델 다운로드 하기
```
<https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF>에서 llama-2-7b-chat.Q4_K_M.gguf를 다운로드 해줍니다.
다운로드한 모델을 아까 만든 models에 넣습니다.
```


최종적으로 다음과 같은 디렉토리 구성이 되어야 합니다.
```
kiosk-llama/
├── app.py
├── bin/
│   └── llama-cli
├── models/
│   └── llama-2-7b-chat.Q4_K_M.gguf
├── static/
├── templates/
│   └── main.html
├── requirements.txt
└── .gitignore
```

실행시키기  
`python3 app.py`

***