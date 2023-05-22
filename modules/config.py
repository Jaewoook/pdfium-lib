# general
debug = False
task = ""

# pdfium
pdfium_git_branch = "5782"
pdfium_git_commit = "4a5e28a78c2dda8033481a0b351953dceb8116fb"
# ^ ref: https://pdfium.googlesource.com/pdfium/+/refs/heads/chromium/5782
# OBS 1: don't forget change in android docker file (docker/android/Dockerfile)
# OBS 2: don't forget change in wasm docker file (docker/wasm/Dockerfile)

# emsdk
emsdk_version = "3.1.39"
# OBS 1: don't forget change in wasm docker file (docker/wasm/Dockerfile)

# macos
configurations_macos = ["release"]
targets_macos = [
    {"target_os": "macos", "target_cpu": "x64", "pdfium_os": "mac"},
    {"target_os": "macos", "target_cpu": "arm64", "pdfium_os": "mac"},
]

# ios
configurations_ios = ["release"]
targets_ios = [
    {
        "target_os": "ios",
        "target_cpu": "arm64",
        "pdfium_os": "ios",
        "target_environment": "device",
    },
    {
        "target_os": "ios",
        "target_cpu": "x64",
        "pdfium_os": "ios",
        "target_environment": "simulator",
    },
    {
        "target_os": "ios",
        "target_cpu": "arm64",
        "pdfium_os": "ios",
        "target_environment": "simulator",
    },
]

# android
configurations_android = ["release"]
targets_android = [
    {
        "target_os": "android",
        "target_cpu": "arm",
        "pdfium_os": "android",
        "android_cpu": "armeabi-v7a",
    },
    {
        "target_os": "android",
        "target_cpu": "x86",
        "pdfium_os": "android",
        "android_cpu": "x86",
    },
    {
        "target_os": "android",
        "target_cpu": "arm64",
        "pdfium_os": "android",
        "android_cpu": "arm64-v8a",
    },
    {
        "target_os": "android",
        "target_cpu": "x64",
        "pdfium_os": "android",
        "android_cpu": "x86_64",
    },
]

# wasm
configurations_wasm = ["release"]
# configurations_wasm = ["debug"]
targets_wasm = [
    {"target_os": "wasm32", "target_cpu": "wasm", "pdfium_os": "wasm"},
]
