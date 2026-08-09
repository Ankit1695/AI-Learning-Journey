# AI Project Setup Commands

## 1. Go to the Week Folder

```powershell
cd week1
```

## 2. Create a New Project

```powershell
uv init day3
```

## 3. Open the Project

```powershell
cd day3
```

## 4. Create a Virtual Environment

```powershell
uv venv --python 3.14
```

## 5. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## 6. Install Dependencies

```powershell
uv add groq python-dotenv
```

## 7. Create `.env`

Add your API keys.

## 8. Create `tokens.py`

## 9. Run the Program

```powershell
python tokens.py
```

- `uv init` → Create a new Python project.
- `uv venv` → Create a virtual environment.
- `Activate.ps1` → Activate the virtual environment.
- `uv add` → Install project dependencies.
- `.env` → Store API keys securely.
- `python <file>.py` → Run a Python file.
