import sys
import subprocess
import platform

def create_venv():
    print("\n🐍 Criando ambiente virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    pip = "venv/Scripts/pip.exe" if platform.system() == "Windows" else "venv/bin/pip"
    python_path = "venv/Scripts/python.exe" if platform.system() == "Windows" else "venv/bin/python"
    print("📦 Instalando dependências...")
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.run([pip, "install", "-r", "requirements.txt"])
    print("✅ Ambiente virtual criado com sucesso!\n")

def activate_help():
    if platform.system() == "Windows":
        print("\n💡 Para ativar o ambiente virtual, use: (PowerShell/CMD) .\\venv\\Scripts\\activate\n")
    else:
        print("\n💡 Para ativar o ambiente virtual, use: (Linux/macOS) source ./venv/bin/activate\n")

def train():
    print("\n💫 Iniciando treinamento do modelo ExtraTrees...")
    subprocess.run([sys.executable, "downscaling/train.py"])

def predict():
    print("\n✨ Informe os campos necessários para predição:")
    ano = input("🔍️ Ano: ")
    mes = input("🔍️ Mês: ")
    lat = input("🔍️ Latitude: ")
    lon = input("🔍️ Longitude: ")
    print(f"🔮 Fazendo previsão para ({ano}, {mes}, {lat}, {lon})...")
    subprocess.run([sys.executable, "downscaling/predict.py", ano, mes, lat, lon])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n📖 Comandos disponíveis: venv | activate | train | predict\n")
        sys.exit(1)

    command = sys.argv[1]

    if command == "venv":
        create_venv()
    elif command == "activate":
        activate_help()
    elif command == "train":
        train()
    elif command == "predict":
        predict()
    else:
        print("\n❌ Comando desconhecido. Use: venv | activate | train | predict\n")
