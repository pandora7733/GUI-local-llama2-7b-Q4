from flask import Flask, request, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("question", "").strip()

    if not user_input:
        return jsonify({"answer": "질문을 입력해주세요."})

    llama_path = os.path.join("bin", "llama-cli")
    model_path = os.path.join("models", "llama-2-7b-chat.Q4_K_M.gguf")

    try:
        result = subprocess.run(
            [llama_path, "-m", model_path,
             "-p", user_input, "--color", "--temp", "0.7", "--n-predict", "128"],
            capture_output=True,
            text=True,
            errors="ignore"  # 인코딩 문제 방지
        )
        output = result.stdout.strip()

        if result.returncode != 0:
            return jsonify({"answer": f"실행 오류 발생: {result.stderr.strip()}"})

        return jsonify({"answer": output})
    except FileNotFoundError:
        return jsonify({"answer": "llama-cli 파일을 찾을 수 없습니다. 경로를 확인해주세요."})
    except Exception as e:
        return jsonify({"answer": f"예외 발생: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)