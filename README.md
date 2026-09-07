# Rafeeq (رفيق)

### AI-Powered Arabic Voice Companion for Older Adults

Rafeeq is an accessible, voice-first companion designed to support older adults in Saudi Arabia with everyday tasks, reminders, religious services, emergency support, and simple daily assistance.

The project focuses on making digital services easier to use through **Saudi Arabic voice interaction**, a simplified Arabic interface, large readable elements, and AI-assisted intent understanding.

---

## ✨ Key Features

- 🎙️ **Voice-First Interaction** — speech-to-text, intent recognition, and spoken Arabic responses
- 💊 **Medication & Appointment Reminders** — support for daily schedules and important reminders
- 🕌 **Prayer Times** — daily prayer times and reminder settings
- 📖 **Quran** — access to Surahs with audio playback
- 🆘 **Emergency Support** — quick access to emergency assistance
- 📍 **Nearby Services** — support for locating mosques, hospitals, and pharmacies
- 👨‍👩‍👧 **Family Contacts** — convenient access to family contact and location options
- 🧠 **Memory Games** — simple cognitive activities such as card matching and color memory
- ♿ **Accessible UI** — Arabic RTL design, large interface elements, readable typography, and reduced visual complexity

---

## 🤖 AI & Voice Flow

Rafeeq is designed around a simple voice interaction pipeline:

`Arabic Voice Input → Speech-to-Text → AI Intent Understanding → Requested Service / Response → Arabic Voice Output`

The repository includes API smoke tests for the AI and voice components used during development.

---

## 🛠️ Technologies

- **FlutterFlow** — application UI and prototype development
- **Firebase / Firestore** — backend services and user data
- **Gemini** — AI-assisted interaction and intent understanding
- **Speech-to-Text (STT)** — Arabic voice transcription
- **Text-to-Speech (TTS)** — spoken Arabic responses
- **Python** — API integration and smoke testing

---

## 🎨 UI/UX & Accessibility

The interface was designed specifically with older adults in mind.

Key design principles include:

- Simple and consistent navigation
- Clear Arabic typography and RTL layout
- Large, recognizable interface elements
- Reduced visual complexity
- Voice-first interaction
- Easy access to frequently used services

For more details, see **[Rafeeq UI Showcase](Rafeeq_UI_Showcase.md)** and the application interfaces included in this repository.

---

## 🔎 Research & Requirements

The project development process included user research, functional and non-functional requirements, interface design, data modeling, and business-model planning.

Repository documentation includes:

- **Interview & Survey Report**
- **Functional & Non-Functional Requirements**
- **Business Model Canvas**
- **FlutterFlow UI Implementation**
- **UI Showcase**
- **ER Diagram**
- **Intent Dataset**

---

## 🧪 API Testing

The repository contains smoke tests for key AI and voice services:

- `test_gemini.py`
- `test_speech_to_text.py`
- `test_text_to_speech.py`

See **[API Smoke Tests](API_SMOKE_TESTS.md)** for additional details.

---

## 📁 Repository Overview

```text
Rafeeq-App/
├── dataset/                              # Intent / voice interaction data
├── API_SMOKE_TESTS.md                    # API testing documentation
├── FlutterFlow_UI_Implementation.md      # UI implementation notes
├── Functional_and_NonFunctional_Requirements.md
├── Rafeeq_Interview_and_Survey_Report.pdf
├── Rafeeq_UI_Showcase.md
├── Business Model Canvas — Rafeeq (رفيق).pdf
├── rafeeq_er_diagram_updated (1).png
├── test_gemini.py
├── test_speech_to_text.py
└── test_text_to_speech.py
```

---

## 🌱 Project Goal

Rafeeq explores how accessible design and AI-powered voice interaction can make everyday digital assistance more approachable for older adults, while keeping the experience simple, familiar, and centered around their daily needs.

---

**Rafeeq | رفيق — Technology designed with accessibility, simplicity, and companionship in mind.**
