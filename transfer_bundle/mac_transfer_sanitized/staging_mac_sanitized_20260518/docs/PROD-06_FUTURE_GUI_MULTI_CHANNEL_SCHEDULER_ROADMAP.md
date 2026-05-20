# PROD-06: Future GUI, Multi-Channel Scheduler & Orchestration Roadmap

**Document Type**: Strategic UI/UX + Automation Architecture  
**Phase**: PROD-06 (After PROD-03/04/05)  
**Status**: DESIGN_ONLY — Not yet implemented  
**Last Updated**: 2026-05-06  
**Audience**: Founder (vision), Builder (UI implementation), Operator (scheduler automation)

---

## EXECUTIVE SUMMARY

Currently, Shadow Creator OS is controlled via:
1. **Open WebUI Chat** (input task → receive dossier)
2. **Operator API** (PowerShell/curl commands)
3. **n8n UI** (view workflow execution)

**PROD-06 adds**:
- **Custom GUI Dashboard** (18 screens with role-based access, real-time monitoring)
- **Multi-Channel Orchestration** (repurpose content across YouTube, Instagram, TikTok, LinkedIn, Blog, Podcast, Newsletter)
- **Automated Scheduler** (daily/weekly content generation, publishing, analytics feedback loop)

This document defines:
- **17 Future GUI Screens** (detailed wireframes and data bindings)
- **Multi-Channel Content Strategy** (platform-specific adaptation, format conversion, approval workflow)
- **11 Automated Scheduler Modes** (from daily topic hunting to cost monitoring)
- **Architecture Enforcement Rule** (GUI/Scheduler → Operator API only, never direct provider access)

---

## PART 1: FUTURE GUI ARCHITECTURE (17 Screens)

### 1.1 GUI Overview & Navigation

**Current State (PROD-01)**:
- Open WebUI: Single chat input
- Operator API: CLI commands only
- n8n: Workflow editor (technical users only)

**Future State (PROD-06)**:
- **Custom Shadow GUI**: 17 integrated screens
  - Role-based sidebar navigation
  - Real-time dossier/packet monitoring
  - Approval & decision workflows
  - Cost tracking & budget management
  - Channel calendar & scheduler
  - Analytics dashboard & feedback loop

**Design Principles**:
- ✅ All controls route through Operator API (never direct n8n/provider calls)
- ✅ Real-time data updates (5-10 sec refresh for observability screens)
- ✅ Mobile-responsive (works on tablet, desktop)
- ✅ Accessibility (WCAG 2.1 AA standard)
- ✅ Audit trail visible (user can see who approved what, when)

### 1.2 Screen Hierarchy & Navigation

```
┌─────────────────────────────────────────────────────┐
│  Shadow Creator OS — Custom Dashboard               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Sidebar (Role-Based):                              │
│  ├─ Overview                    (Founder/Operator) │
│  ├─ Create Content              (Creator)          │
│  │  ├─ Task Builder             (New)              │
│  │  └─ Mode Launcher            (New)              │
│  ├─ Manage Dossiers             (Creator/Founder)  │
│  │  ├─ Dossier Browser          (New)              │
│  │  ├─ Packet Viewer            (New)              │
│  │  └─ Output Viewer            (New)              │
│  ├─ Publish & Schedule          (Creator/Founder)  │
│  │  ├─ Channel Calendar         (New)              │
│  │  └─ Publishing Queue         (New)              │
│  ├─ Approval & Workflows        (Founder/Operator) │
│  │  ├─ Approval Screen          (Enhanced)         │
│  │  ├─ Remodify Screen          (New)              │
│  │  ├─ Replay Control           (New)              │
│  │  └─ Workflow Progress Tree   (New)              │
│  ├─ Monitoring & Alerts         (Operator)         │
│  │  ├─ Alert Center             (New)              │
│  │  ├─ Provider Bridge Monitor  (New)              │
│  │  └─ Cost/Budget Monitor      (New)              │
│  ├─ Intelligence & Feedback     (All)              │
│  │  ├─ Weekly Briefing View     (New)              │
│  │  ├─ Analytics Dashboard      (New)              │
│  │  └─ Scheduler Console        (Founder)          │
│  └─ Settings                    (Founder/Creator)  │
│     ├─ Credentials              (New)              │
│     ├─ Budget & Costs           (New)              │
│     ├─ Channel Preferences      (New)              │
│     └─ Approval Policies        (Founder only)     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## PART 2: 17 FUTURE GUI SCREENS (Detailed)

### Screen 1: Dashboard Overview (Enhanced)

**Current**: Empty stub in PROD-01  
**Future (PROD-06)**: Real-time status center

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Dashboard: Today's Activity                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│ [Active Dossiers]  [Pending Approvals]  [Errors]  │
│      3 running           2 waiting         1 new  │
│                                                     │
│ ┌──────────────────────────────────────────────┐  │
│ │ Dossier Pipeline (Real-time)                 │  │
│ │ ├─ WF-100 (1): AI trends research (45%)      │  │
│ │ ├─ WF-200 (2): YouTube script (30%)          │  │
│ │ └─ WF-610 (1): Voice synthesis (5%)          │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
│ ┌──────────────────────────────────────────────┐  │
│ │ Today's Budget Spent: $3.45 of $50.00        │  │
│ │ ████████░░░░░░░░░░░░░░░░░░ 7% used          │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
│ ┌──────────────────────────────────────────────┐  │
│ │ Recent Activity                              │  │
│ │ 14:32 - Dossier-005 approved by founder      │  │
│ │ 14:28 - WF-610 completed (ElevenLabs voice) │  │
│ │ 14:15 - New dossier created: AI trends      │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Data Binding**:
- Real-time count of dossiers by status (from `/operator/dossier/list`)
- Pipeline visualization (current workflow stage for each dossier)
- Daily budget spent (from cost_tracking in all dossiers)
- Recent audit trail entries (from `/operator/events`)

**Refresh Rate**: 5 sec (real-time feel)

---

### Screen 2: Create Content — Task Builder

**Purpose**: User-friendly task creation (alternative to Open WebUI chat)

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Create New Content Task                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Step 1: Basic Info                                 │
│ ┌──────────────────────────────────────────────┐   │
│ │ Content Title:                               │   │
│ │ [AI Trends in 2026________________]          │   │
│ │                                              │   │
│ │ Topic Description:                           │   │
│ │ [Research latest developments in AI, focus   │   │
│ │  on LLMs, agents, and enterprise adoption]   │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Step 2: Content Format                             │
│ ┌──────────────────────────────────────────────┐   │
│ │ Platform: [v YouTube Long-Form]              │   │
│ │           [  YouTube Shorts ]                │   │
│ │           [  Instagram Reel ]                │   │
│ │           [  LinkedIn Post ]                 │   │
│ │           [  Blog Article ]                  │   │
│ │           [  Podcast Audio ]                 │   │
│ │           [  Newsletter ]                    │   │
│ │                                              │   │
│ │ Duration: [10-15 minutes_]                   │   │
│ │ Tone: [  Professional v]                    │   │
│ │ Audience: [Tech enthusiasts v]               │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Step 3: Advanced Options (Optional)                │
│ ┌──────────────────────────────────────────────┐   │
│ │ [x] Include voice synthesis                  │   │
│ │ [x] Add avatar video                         │   │
│ │ [ ] Include AI debate                        │   │
│ │ [ ] Multi-language versions                  │   │
│ │ [ ] Include images (DALL-E)                  │   │
│ │                                              │   │
│ │ Budget Max: [$5.00________]                  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [Back] [Save Draft] [Create Task →]               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Form-based task creation (clearer than Open WebUI chat for complex tasks)
- Platform selection (create once, repurpose multiple ways)
- Duration/tone/audience selection
- Advanced option toggles (voice, avatar, images, etc.)
- Budget setting
- Submit: POST /operator/new-content-job with all fields

**Data Binding**:
- Dropdown options from registries (available platforms, tones, audiences)
- User's current budget_remaining displayed
- Save draft to localStorage (allows recovery if session crashes)

---

### Screen 3: Mode Launcher

**Purpose**: Select operating mode (Creator/Founder/Builder/Operator) and operational modes

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Operating Mode Selector                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Current Mode: Creator                              │
│                                                     │
│ Switch Operating Mode:                             │
│ ┌──────────────────────────────────────────────┐   │
│ │ [ ] Creator    - Create and refine content   │   │
│ │     (Your current mode)                      │   │
│ │                                              │   │
│ │ [x] Founder    - Approve & govern            │   │
│ │                                              │   │
│ │ [ ] Builder    - Debug & optimize            │   │
│ │                                              │   │
│ │ [ ] Operator   - Monitor & maintain          │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Operational Modes (Can combine):                   │
│ ┌──────────────────────────────────────────────┐   │
│ │ [ ] Alert Mode         - Monitor errors      │   │
│ │ [ ] Troubleshoot Mode  - Debug workflows     │   │
│ │ [x] Safe Mode          - Restrict operations │   │
│ │ [ ] Analysis Dashboard - View metrics        │   │
│ │ [ ] Self-Learning      - Autonomous optimize │   │
│ │ [ ] Debug Mode         - Verbose logging     │   │
│ │ [ ] Context Engineering- Prompt tuning       │   │
│ │ [ ] Replay Mode        - Re-execute stages   │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Module Selector:                                   │
│ ┌──────────────────────────────────────────────┐   │
│ │ Runtime Environment:                         │   │
│ │ ( ) Local     - Ollama only                  │   │
│ │ (x) Hybrid    - Local + Cloud speedup        │   │
│ │ ( ) Cloud     - Cloud-first                  │   │
│ │                                              │   │
│ │ When switching:                              │   │
│ │ [Founder approval required]                  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [Save Mode Selection]                              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Switch between 4 operating modes
- Enable/disable operational modes (with consent checkboxes if required)
- Select runtime module (Local/Hybrid/Cloud)
- Each mode change: POST /operator/modes/set
- Founding-mode-only changes require founder password confirmation

---

### Screen 4: Dossier Browser

**Purpose**: List all dossiers with filtering, sorting, search

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Dossier Library                                     │
├─────────────────────────────────────────────────────┤
│ [Search: ________________] [Status v] [Date v]    │
│                                                     │
│ ┌─────────────────────────────────────────────┐    │
│ │ Dossier-005     Status: APPROVED_BY_FOUNDER │    │
│ │ Topic: AI Trends in 2026                    │    │
│ │ Created: 2026-05-05 14:20                   │    │
│ │ Progress: ████████████████████░░░░ 95%      │    │
│ │ Workflow: WF-200 (Script Generation)        │    │
│ │ Packets: 3/5 generated                      │    │
│ │ Cost: $2.43 / Budget: $5.00                 │    │
│ │ [View Details] [View Packets] [Download]    │    │
│ └─────────────────────────────────────────────┘    │
│                                                     │
│ ┌─────────────────────────────────────────────┐    │
│ │ Dossier-004     Status: READY_FOR_APPROVAL  │    │
│ │ Topic: Machine Learning Fundamentals         │    │
│ │ Created: 2026-05-05 10:15                   │    │
│ │ Progress: ██████████████████░░░░░░ 85%      │    │
│ │ Workflow: WF-610 (Voice Synthesis)          │    │
│ │ Packets: 4/5 generated                      │    │
│ │ Cost: $1.85 / Budget: $5.00                 │    │
│ │ [View Details] [Approve] [Request Changes]  │    │
│ └─────────────────────────────────────────────┘    │
│                                                     │
│ ┌─────────────────────────────────────────────┐    │
│ │ Dossier-003     Status: TOPIC_RESEARCH_RUNNING  │
│ │ Topic: Quantum Computing Breakthroughs       │    │
│ │ Created: 2026-05-05 09:00                   │    │
│ │ Progress: ███████░░░░░░░░░░░░░░░░░░░░░░░░░ 35% │
│ │ Workflow: WF-100 (Topic Intelligence)       │    │
│ │ Packets: 1/5 generated                      │    │
│ │ Cost: $0.00 (in progress)                   │    │
│ │ [View Details] [Monitor]                    │    │
│ └─────────────────────────────────────────────┘    │
│                                                     │
│ [← Previous] [1] [2] [3] [→ Next]                  │
│ Showing 3 of 47 dossiers                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Search: by topic, dossier_id
- Filter: by status, date, cost range
- Sort: by date (newest/oldest), status, cost
- Pagination: 10 dossiers per page
- Data binding: GET /operator/dossier/list?filters=...

---

### Screen 5: Packet Viewer

**Purpose**: Inspect detailed content of generated packets (research, scripts, metadata)

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Dossier-005: Packet Viewer                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Packet Flow Diagram:                               │
│                                                     │
│ ┌──────────┐    ┌──────────┐    ┌──────────┐      │
│ │  pkt_100 │ -> │  pkt_200 │ -> │  pkt_610 │      │
│ │ Research │    │  Script  │    │  Voice   │      │
│ │   ✅     │    │   ✅     │    │   ✅     │      │
│ └──────────┘    └──────────┘    └──────────┘      │
│                                                     │
│ Selected Packet: pkt_200 (Script)                  │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Content:                                     │   │
│ │                                              │   │
│ │ [HOOK]                                       │   │
│ │ "Did you know AI models like GPT-4 are now  │   │
│ │  outperforming humans in certain tasks?"     │   │
│ │                                              │   │
│ │ [BODY]                                       │   │
│ │ "In 2026, we're seeing AI adoption across   │   │
│ │  enterprise sectors..."                      │   │
│ │                                              │   │
│ │ [CTA]                                        │   │
│ │ "What's your view on AI? Comment below!"     │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Metadata:                                          │
│ Word Count: 1,850  |  Readability: 8.2 (Grade 8)  │
│ Generated by: WF-200 (Script Generation)           │
│ Model: Ollama Llama 3.2                            │
│ Generated at: 2026-05-05 14:32:15                  │
│ Cost: $0.00                                        │
│                                                     │
│ [Edit] [Request Remodify] [Download as .docx]     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Visual packet flow diagram (which packets exist, which are pending)
- Display content for each packet (Research, Script, Metadata, Voice, Images, Video)
- Metadata inspection (word count, readability, model used, cost, timestamp)
- Edit/Remodify/Download options
- Data binding: GET /operator/dossier/:id (returns full dossier with all packets)

---

### Screen 6: Output Viewer (Media Preview)

**Purpose**: Preview generated media (voice, images, video)

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Dossier-005: Output Viewer                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Available Outputs:                                 │
│ [ ] pkt_100 - Research Document  (view)           │
│ [x] pkt_200 - Script Text        (view)           │
│ [x] pkt_610 - Voice Audio        (play)           │
│ [x] pkt_620 - Image (DALL-E)    (view)           │
│ [ ] pkt_650 - Avatar Video       (view)           │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Selected: pkt_610 - Voice Audio              │   │
│ │                                              │   │
│ │ [▶ PLAY]  [↻ LOOP]  [↙ DOWNLOAD]            │   │
│ │                                              │   │
│ │ Audio Player:                                │   │
│ │ ██████████░░░░░░░░░░░░░░░░░░░░ 2:35 / 4:20 │   │
│ │                                              │   │
│ │ Metadata:                                    │   │
│ │ Duration: 4:20 (260 seconds)                 │   │
│ │ Provider: ElevenLabs                         │   │
│ │ Voice ID: alloy                              │   │
│ │ File Size: 1.2 MB                            │   │
│ │ Cost: $0.15                                  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Selected: pkt_620 - Image                    │   │
│ │                                              │   │
│ │ [Image Preview]                              │   │
│ │ DALL-E generated image: "AI future 2026"     │   │
│ │                                              │   │
│ │ ┌─────────────────────────────────────────┐  │   │
│ │ │                                         │  │   │
│ │ │      [1024x1024 Image Preview]          │  │   │
│ │ │                                         │  │   │
│ │ └─────────────────────────────────────────┘  │   │
│ │                                              │   │
│ │ Provider: DALL-E 3                           │   │
│ │ Cost: $0.12                                  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Preview/play all generated media
- Audio player with progress bar
- Image viewer with zoom
- Video player (for WF-650 avatar, WF-640 video)
- Download buttons for each output
- Metadata display (duration, file size, provider, cost)

---

### Screen 7: Channel Calendar & Publishing Queue

**Purpose**: Plan content for multiple channels, schedule publishing

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Channel Calendar & Publishing Queue                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Channels: [YouTube v] [Instagram v] [LinkedIn v]   │
│ View: [Month] [Week] [Day]                          │
│                                                     │
│                   MAY 2026                          │
│ ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐       │
│ │ Sun │ Mon │ Tue │ Wed │ Thu │ Fri │ Sat │       │
│ ├─────┼─────┼─────┼─────┼─────┼─────┼─────┤       │
│ │  3  │  4  │  5  │  6  │  7  │  8  │  9  │       │
│ │     │     │ ★★★ │ ★★★ │ ★   │     │     │       │
│ ├─────┼─────┼─────┼─────┼─────┼─────┼─────┤       │
│ │ 10  │ 11  │ 12  │ 13  │ 14  │ 15  │ 16  │       │
│ │ ★   │ ★★  │ ★   │     │ ★   │ ★★★ │ ★★  │       │
│ └─────┴─────┴─────┴─────┴─────┴─────┴─────┘       │
│                                                     │
│ ★ = Content scheduled                              │
│ ★★ = Multiple pieces same day                       │
│ ★★★ = Heavy publication day                         │
│                                                     │
│ Selected Day: May 5, 2026 (3 pieces scheduled)     │
│ ┌──────────────────────────────────────────────┐   │
│ │ 09:00 - Dossier-005 → YouTube (long-form)   │   │
│ │         Status: APPROVED, Ready to publish   │   │
│ │         [Publish Now] [Postpone] [Cancel]    │   │
│ │                                              │   │
│ │ 14:00 - Dossier-004 → Instagram (Reel)      │   │
│ │         Status: APPROVED, Pending conversion │   │
│ │         [Convert & Publish] [Cancel]        │   │
│ │                                              │   │
│ │ 18:00 - Dossier-006 → LinkedIn (Article)    │   │
│ │         Status: DRAFT, Needs approval        │   │
│ │         [Submit for Approval] [Edit]         │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Publishing Queue (Pending):                        │
│ ┌──────────────────────────────────────────────┐   │
│ │ 5 items waiting for approval/conversion      │   │
│ │ 3 items scheduled for automated publish      │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Multi-channel calendar view (YouTube, Instagram, TikTok, LinkedIn, Blog, Podcast, Newsletter)
- Drag-and-drop dossiers to calendar dates
- Automatic format conversion (YouTube → Instagram Reel, Blog, Podcast, etc.)
- Publishing queue with status (Approved, Pending Approval, Ready to Publish)
- One-click publish (triggers WF-660 workflow)
- Scheduled publishing (queue for future date/time)

---

### Screen 8: Approval Screen (Enhanced)

**Purpose**: Founder reviews and approves/rejects/requests changes

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Approval Queue — Founder Review                     │
├─────────────────────────────────────────────────────┤
│ Queue: 2 items pending approval                     │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Dossier-004 - "Machine Learning Fundamentals"│   │
│ │ Status: READY_FOR_APPROVAL                   │   │
│ │ Created: 2026-05-05 10:15 (4 hours ago)      │   │
│ │ Submitted for approval at: 2026-05-05 14:15  │   │
│ │                                              │   │
│ │ Content Preview:                             │   │
│ │ ┌──────────────────────────────────────────┐ │   │
│ │ │ SCRIPT:                                  │ │   │
│ │ │ "Did you know machine learning powers... │ │   │
│ │ │                                          │ │   │
│ │ │ Length: 1,200 words (8 min read)         │ │   │
│ │ │                                          │ │   │
│ │ │ VOICE: [▶ PLAY AUDIO]                   │ │   │
│ │ │ Duration: 4:20 (ElevenLabs, $0.15)       │ │   │
│ │ │                                          │ │   │
│ │ │ IMAGE: [View DALL-E Image]               │ │   │
│ │ │ DALL-E 3 generated ($0.12)               │ │   │
│ │ │                                          │ │   │
│ │ │ AVATAR: [View Preview Video]             │ │   │
│ │ │ HeyGen avatar video, 4:20 ($2.00)        │ │   │
│ │ └──────────────────────────────────────────┘ │   │
│ │                                              │   │
│ │ Cost Breakdown:                              │   │
│ │ Voice (ElevenLabs):    $0.15                 │   │
│ │ Image (DALL-E):        $0.12                 │   │
│ │ Avatar (HeyGen):       $2.00                 │   │
│ │ ────────────────────────────                │   │
│ │ Total:                 $2.27                 │   │
│ │ User Budget Remaining: $2.73                 │   │
│ │                                              │   │
│ │ Founder Decision:                            │   │
│ │ ┌──────────────────────────────────────────┐ │   │
│ │ │ [✅ APPROVE]                             │ │   │
│ │ │ [📝 REQUEST CHANGES]                     │ │   │
│ │ │ [❌ REJECT]                              │ │   │
│ │ │                                          │ │   │
│ │ │ Notes (optional): [________________]     │ │   │
│ │ └──────────────────────────────────────────┘ │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Dossier-005 - "AI Trends in 2026"            │   │
│ │ Status: READY_FOR_APPROVAL                   │   │
│ │ [View] [Approve] [Request Changes] [Reject]  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Display full dossier content (script, voice preview, images, video)
- Cost breakdown by provider
- Three decision options:
  1. **APPROVE**: Dossier moves to APPROVED_BY_FOUNDER → WF-020 (approval handler)
  2. **REQUEST CHANGES**: Founder writes instructions, WF-021 (replay) triggered, auto-rerun
  3. **REJECT**: Dossier archived, creator notified
- Notes field for Founder feedback (logged to audit_trail)
- Data binding: GET /operator/dossier/:id, POST /operator/approve/:id, etc.

---

### Screen 9: Remodify Screen (Request Changes)

**Purpose**: Founder specifies what to change, system regenerates content

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Request Changes — Dossier-004                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Current Content: Script (1,200 words, 8 min read)  │
│                                                     │
│ What would you like changed?                        │
│ ┌──────────────────────────────────────────────┐   │
│ │ [x] Script  [ ] Voice  [ ] Images  [ ] Video │   │
│ │                                              │   │
│ │ Feedback for Script Regeneration:            │   │
│ │ ┌──────────────────────────────────────────┐ │   │
│ │ │ [Textarea: 500 char limit]               │ │   │
│ │ │                                          │ │   │
│ │ │ "Make the script shorter (under 5 min),  │ │   │
│ │ │  add more humor, and emphasize practical │ │   │
│ │ │  use cases rather than theory"           │ │   │
│ │ │                                          │ │   │
│ │ │ Estimated new cost: $0.00 (rerun Ollama) │ │   │
│ │ │ New budget remaining: $2.73               │ │   │
│ │ └──────────────────────────────────────────┘ │   │
│ │                                              │   │
│ │ [Change Script Only]  [Change Everything]   │   │
│ │                                              │   │
│ │ Expected timeline:                           │   │
│ │ ⏱ Script regeneration: 1-2 minutes           │   │
│ │ ⏱ Voice re-synthesis: 30 seconds (if changed)│   │
│ │ ⏱ Total: ~2 minutes                          │   │
│ │                                              │   │
│ │ [Cancel] [Submit Changes & Rerun]            │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Select which packets to regenerate (Script, Voice, Images, Video)
- Text area for Founder instructions (natural language feedback)
- Cost estimation (show new cost if regeneration required)
- Timeline estimate (how long for changes to complete)
- Submit: POST /operator/remodify/:id → triggers WF-021 (replay)
- Dossier status: REMODIFICATION_IN_PROGRESS → back to normal flow when done

---

### Screen 10: Replay Control

**Purpose**: Operator/Founder can manually re-execute a specific workflow stage

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Replay Control — Dossier-003                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Execution History:                                 │
│ ┌──────────────────────────────────────────────┐   │
│ │ WF-001 (Dossier Create)      ✅ 2026-05-05 │   │
│ │ WF-100 (Topic Intelligence)  ❌ 2026-05-05 │   │
│ │                   ERROR: Ollama timeout      │   │
│ │ WF-200 (Script Generation)   ⏸ WAITING     │   │
│ │ WF-300 (Metadata Planning)   ⏸ BLOCKED     │   │
│ │ WF-400 (Production Planning) ⏸ BLOCKED     │   │
│ │ WF-500 (Publishing Prep)     ⏸ BLOCKED     │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Replay Failed Stage:                               │
│ ┌──────────────────────────────────────────────┐   │
│ │ Stage to Replay: [WF-100 (Topic Intelligence)v] │   │
│ │                                              │   │
│ │ Instructions for Retry:                      │   │
│ │ [Use shorter research scope______________]   │   │
│ │                                              │   │
│ │ Max Retry Attempts: [3_____]                 │   │
│ │                                              │   │
│ │ Starting From: [Latest Checkpoint] ✓         │   │
│ │               [Fresh Start] ○                 │   │
│ │                                              │ │   │
│ │ Cost Estimate for Replay: $0.00              │   │
│ │ (Ollama local, no provider charge)           │   │
│ │                                              │   │
│ │ Estimated Duration: 1-2 minutes              │   │
│ │                                              │   │
│ │ [Analyze Error] [Replay Now]                 │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Error Details:                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Error Message: "Timeout waiting for Ollama   │   │
│ │  response after 30 seconds"                  │   │
│ │                                              │   │
│ │ Error Log:                                   │   │
│ │ [View Full Trace]                            │   │
│ │                                              │   │
│ │ Suggestions:                                 │   │
│ │ - Check Ollama status: `npm run health:check`│   │
│ │ - Restart Ollama: `killall ollama`           │   │
│ │ - Try replay with reduced scope               │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Execution history (green checkmark = success, red X = failed, blue = pending)
- Replay selection (which stage to re-execute)
- Instructions field (for Founder to adjust parameters)
- Retry limit (max 3 attempts to prevent infinite loops)
- Checkpoint selection (replay from where it failed, or start fresh)
- Cost estimate (show if provider calls will incur charges)
- Duration estimate
- Error analysis (show full stack trace)
- Troubleshooting suggestions (links to runbook)

**Triggering Replay**:
- POST /operator/replay/:id with stage=WF-100, instructions=..., checkpoint=latest
- Dossier status: REPLAY_RUNNING
- System re-executes WF-100, generates new outputs, saves to dossier
- Back to READY_FOR_APPROVAL when complete

---

### Screen 11: Workflow Progress Tree

**Purpose**: Real-time visualization of workflow execution (DAG format)

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Workflow Progress Tree — Dossier-005                │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Real-time Execution (Auto-updates every 2 sec)     │
│                                                     │
│          ┌─ WF-001 ───────────┐                    │
│          │ Dossier Create     │ ✅ 10s (DONE)     │
│          └─ WF-010 ───────────┘                    │
│             Router             ✅ 5s (DONE)        │
│             │                                       │
│    ┌────────┴────────┐                             │
│    │                 │                              │
│    v                 v                              │
│  WF-100           WF-100-ALT                        │
│  Topic Intel      (Cloud GPT-4)                     │
│  (Ollama)         ⏳ RUNNING (45s elapsed)         │
│  ✅ DONE                                            │
│  (45s)            ETA: 15s more                     │
│    │                 │                              │
│    └────────┬────────┘                             │
│             v                                       │
│           WF-200                                    │
│       Script Generation                             │
│       (Ollama or GPT-4)                             │
│       ⏳ WAITING for WF-100-ALT                     │
│                                                     │
│    (WF-300, WF-400, WF-500 blocked until WF-200)  │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ WF-100 Result: 850 research points found    │   │
│ │ Sources: 12 credible references              │   │
│ │ Confidence score: 0.92                       │   │
│ │ Time: 45 seconds                             │   │
│ │                                              │   │
│ │ WF-100-ALT (Cloud) in progress...            │   │
│ │ Elapsed: 45s, ETA: 15s more                  │   │
│ │ Current operation: Analyzing sources         │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Legend: ✅ Done | ⏳ Running | ⏸ Waiting | ❌ Failed  │
│ (Refresh: 2s)                                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- DAG visualization of workflow dependencies
- Real-time status updates (refresh every 2 sec)
- Color coding (green = done, blue = running, gray = waiting, red = failed)
- Elapsed time & ETA for each stage
- Detailed output panel (show results as workflows complete)
- Dossier state machine (CREATED → TOPIC_RESEARCH → SCRIPT_GENERATION → ... → READY_FOR_APPROVAL)

---

### Screen 12: Alert Center

**Purpose**: Operator/Founder monitor system alerts and errors

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Alert Center — Real-time Monitoring                 │
├─────────────────────────────────────────────────────┤
│ Critical: 1 | Warning: 3 | Info: 5                 │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ 🔴 CRITICAL - Ollama Offline                 │   │
│ │ 14:45 | Dossier-003 (WF-100 timeout)         │   │
│ │                                              │   │
│ │ Impact: 2 dossiers blocked (WF-100)          │   │
│ │ Suggested Action: Restart Ollama             │   │
│ │ [Acknowledge] [Escalate to Founder]          │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ ⚠️  WARNING - High Cost Alert                 │   │
│ │ 14:32 | Daily spend: $47.23 of $50.00 budget │   │
│ │                                              │   │
│ │ Remaining budget: $2.77 (5.5%)                │   │
│ │ Projected overage: Possible if 3+ more       │   │
│ │              avatar videos created           │   │
│ │ [Acknowledge] [Increase Budget] [Block New]  │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ ⚠️  WARNING - Rate Limit (ElevenLabs)         │   │
│ │ 14:20 | 429 Too Many Requests                │   │
│ │                                              │   │
│ │ Will retry in: 60 seconds                    │   │
│ │ Dossier-004 affected: Voice synthesis        │   │
│ │ [Acknowledge]                                │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ℹ️  INFO - WF-200 Completed                        │
│ 14:15 | Dossier-005 script generation done    │   │
│ [Acknowledge]                                      │
│                                                     │
│ Past Alerts (Archive):                             │
│ [Show All] [Clear Resolved]                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Real-time alert feed (critical, warning, info levels)
- Alert acknowledgment (dismiss but keep in history)
- Escalation (notify Founder)
- Suggested actions (links to runbook, manual recovery steps)
- Data binding: GET /operator/alerts
- Auto-refresh: 5 sec

---

### Screen 13: Provider Bridge Monitor

**Purpose**: Track all provider calls (cost, status, errors)

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Provider Bridge Monitor                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Active Provider Calls (Last 24h):                   │
│ ┌──────────────────────────────────────────────┐   │
│ │ Provider      │ Calls │ Success │ Failed │   │   │
│ ├──────────────────────────────────────────────┤   │
│ │ ElevenLabs    │  3    │ 2 (67%) │ 1 (33%)│   │   │
│ │ HeyGen        │  1    │ 1 (100%)│ 0      │   │   │
│ │ DALL-E 3      │  2    │ 2 (100%)│ 0      │   │   │
│ │ OpenAI GPT-4  │  2    │ 2 (100%)│ 0      │   │   │
│ │ OpenRouter    │  0    │ -       │ -      │   │   │
│ │ Ollama        │ 45    │ 44(98%) │ 1 (2%) │   │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Cost Summary (Last 24h):                           │
│ ┌──────────────────────────────────────────────┐   │
│ │ ElevenLabs (3 calls): $0.45                  │   │
│ │ HeyGen     (1 call):  $2.00                  │   │
│ │ DALL-E    (2 calls):  $0.24                  │   │
│ │ OpenAI    (2 calls):  $0.30                  │   │
│ │ Ollama        (free): $0.00                  │   │
│ │ ───────────────────────────────────────────  │   │
│ │ Total (24h):          $2.99                  │   │
│ │ Daily Avg (7 days):   $2.15                  │   │
│ │ Monthly Projection:   $64.50                 │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Failed Calls (Troubleshooting):                    │
│ ┌──────────────────────────────────────────────┐   │
│ │ ElevenLabs (1 failed):                       │   │
│ │ Error: Rate Limit (429)                      │   │
│ │ Dossier: Dossier-004                         │   │
│ │ Time: 14:20                                  │   │
│ │ Status: Retrying...                          │   │
│ │ [View Trace] [Manual Retry]                  │   │
│ │                                              │   │
│ │ Ollama (1 failed):                           │   │
│ │ Error: Timeout after 30s                     │   │
│ │ Dossier: Dossier-003                         │   │
│ │ Time: 13:45                                  │   │
│ │ Status: ⏳ Awaiting Ollama restart           │   │
│ │ [View Trace] [Replay] [Use Fallback]         │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Provider call statistics (success rate, failure count)
- Cost breakdown by provider
- Monthly cost projection
- Failed call troubleshooting (view error, manual retry options)
- Real-time monitoring of active calls

---

### Screen 14: Cost/Budget Monitor

**Purpose**: Track spending, enforce budgets, forecast overages

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Cost & Budget Monitor                               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Today's Spending:                                  │
│ ┌──────────────────────────────────────────────┐   │
│ │ Daily Budget: $50.00                         │   │
│ │ Spent Today: $47.23                          │   │
│ │ Remaining: $2.77 (5.5%)                      │   │
│ │                                              │   │
│ │ ███████████████████████░░░░░ 94.5% used      │   │
│ │                                              │   │
│ │ ⚠️  WARNING: Low budget remaining             │   │
│ │ New dossier with voice/avatar risks overage │   │
│ │                                              │   │
│ │ [Increase Budget] [Block New Creation]       │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Cost by Provider (Today):                          │
│ ┌──────────────────────────────────────────────┐   │
│ │ Ollama (local):          $0.00 (0%)         │   │
│ │ ElevenLabs (voice):      $0.45 (1%)         │   │
│ │ HeyGen (avatar):         $2.00 (4%)         │   │
│ │ DALL-E (images):         $0.24 (<1%)        │   │
│ │ OpenAI (GPT-4):          $0.30 (<1%)        │   │
│ │ Other:                   $44.24 (94%)       │   │
│ │ ───────────────────────────────────────────  │   │
│ │ Total:                   $47.23              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Spending Trend (Last 7 Days):                      │
│ ┌──────────────────────────────────────────────┐   │
│ │ Day 1: $42.50                                │   │
│ │ Day 2: $38.99                                │   │
│ │ Day 3: $51.23 (exceeded budget! Manual fix)  │   │
│ │ Day 4: $45.00                                │   │
│ │ Day 5: $39.50                                │   │
│ │ Day 6: $50.00                                │   │
│ │ Day 7: $47.23 ← Today                       │   │
│ │ Average: $45.35 / day                        │   │
│ │ Monthly Projection: $1,360.50 (over budget!) │   │
│ │                                              │   │
│ │ [Adjust Daily Budget] [Review Spending]      │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Per-Provider Limits:                               │
│ ┌──────────────────────────────────────────────┐   │
│ │ Provider     │ Limit  │ Used  │ Remaining   │   │
│ ├──────────────────────────────────────────────┤   │
│ │ ElevenLabs   │ $30    │ $12   │ $18 (60%)   │   │
│ │ HeyGen       │ $50    │ $30   │ $20 (60%)   │   │
│ │ DALL-E       │ $20    │ $8    │ $12 (60%)   │   │
│ │ OpenAI       │ $40    │ $22   │ $18 (55%)   │   │
│ │ Others       │ TBD    │ ...   │ ...         │   │
│ │                                              │   │
│ │ [Edit Limits] [Set Per-Provider Rules]       │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Daily budget tracking (real-time)
- Spending by provider pie chart
- 7-day trend graph
- Monthly projection
- Per-provider limits with tracking
- Budget alerts (warning when near limit)
- Adjustment controls (increase budget, set provider limits)

---

### Screen 15: Weekly Briefing View

**Purpose**: Executive summary of week's activity, metrics, insights

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Weekly Briefing — Week of May 5, 2026               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ 📊 EXECUTIVE SUMMARY                                │
│ ┌──────────────────────────────────────────────┐   │
│ │ Content Created:  8 dossiers                 │   │
│ │ Content Published: 6 pieces (YouTube, Insta) │   │
│ │ Total Cost:      $47.23                      │   │
│ │ Avg Cost/Dossier: $5.90                      │   │
│ │ Success Rate:     87.5% (7/8 completed)     │   │
│ │ 1 Failed (WF-100 timeout, replayed OK)      │   │
│ │                                              │   │
│ │ Trend: ↑ 15% more content vs week before     │   │
│ │ Trend: ↓ 5% cost reduction (better mix)      │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ 📈 DOSSIER BREAKDOWN                                │
│ ┌──────────────────────────────────────────────┐   │
│ │ Created:   8 dossiers (Mon-Fri)              │   │
│ │ Approved:  6 dossiers (Founder sign-off)     │   │
│ │ Published: 5 dossiers (YouTube, Insta)       │   │
│ │ Pending:   1 dossier (awaiting Founder)      │   │
│ │ Failed:    1 dossier (WF-100 error → fixed)  │   │
│ │                                              │   │
│ │ Topics: AI, ML, Cloud, Security, etc.        │   │
│ │ Avg. Script Length: 1,456 words              │   │
│ │ Avg. Video Duration: 8:32 minutes            │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ 🎯 TOP CHANNELS BY ENGAGEMENT (from analytics)     │
│ ┌──────────────────────────────────────────────┐   │
│ │ YouTube:   2 videos,  4,230 views (avg 2.1k)│   │
│ │ Instagram: 2 reels,   8,900 likes (avg 4.4k)│   │
│ │ LinkedIn:  1 article, 450 clicks              │   │
│ │ Blog:      1 post,    230 visits              │   │
│ │                                              │   │
│ │ Best Performer: Instagram Reel on AI Tips    │   │
│ │ (9,200 likes, 2.3k shares)                   │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ 💰 COST ANALYSIS                                    │
│ ┌──────────────────────────────────────────────┐   │
│ │ ElevenLabs (voice):  $2.10 (4.5%)            │   │
│ │ HeyGen (avatar):     $6.00 (12.7%)           │   │
│ │ DALL-E (images):     $1.44 (3.0%)            │   │
│ │ OpenAI (GPT-4):      $2.85 (6.0%)            │   │
│ │ Ollama (local):      $0.00 (0%)              │   │
│ │ Other/Overhead:      $34.84 (73.8%)          │   │
│ │ ───────────────────────────────────────────  │   │
│ │ Total Week:          $47.23                  │   │
│ │ Budget Alert: None (within budget)           │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ✨ INSIGHTS & RECOMMENDATIONS                       │
│ ┌──────────────────────────────────────────────┐   │
│ │ 1. Instagram outperforming YouTube (higher   │   │
│ │    engagement rate). Consider more Reels.    │   │
│ │                                              │   │
│ │ 2. Avatar videos cost 2x voice-only. ROI      │   │
│ │    strong on Instagram, neutral on LinkedIn. │   │
│ │    Suggest: Avatar for social, voice for     │   │
│ │    long-form YouTube.                        │   │
│ │                                              │   │
│ │ 3. 1 WF-100 timeout. Recommend: Increase     │   │
│ │    Ollama memory allocation (model too large)│   │
│ │    or upgrade to cloud LLM (GPT-4).          │   │
│ │                                              │   │
│ │ 4. Cost trend: Slightly up due to more       │   │
│ │    avatar usage. Sustainable if engagement   │   │
│ │    continues to grow.                        │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [Schedule Next Week] [Export as PDF] [Email to Me] │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- Executive summary (key metrics, trends)
- Dossier breakdown (created, approved, published, failed)
- Top channels by engagement (from YouTube, Instagram, LinkedIn, etc. analytics APIs)
- Cost analysis (breakdown by provider)
- Insights & recommendations (auto-generated based on data)
- Export & email (send briefing report)

---

### Screen 16: Scheduler Console (Founder Only)

**Purpose**: Configure automated content generation & publishing schedules

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Scheduler Console — Automation Rules                │
├─────────────────────────────────────────────────────┤
│ [Active Schedules: 4]  [Create New]                 │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Schedule 1: Daily Topic Hunt                 │   │
│ │ Status: ✅ ACTIVE                            │   │
│ │ Frequency: Daily @ 8:00 AM                   │   │
│ │ Last Run: Today 08:05 (discovered 5 topics)  │   │
│ │ Next Run: Tomorrow 08:00                     │   │
│ │                                              │   │
│ │ Rule: Search trend APIs for top topics       │   │
│ │       Auto-create dossier for top result     │   │
│ │       Assign to: Creator mode                │   │
│ │       Budget per dossier: $10.00             │   │
│ │                                              │   │
│ │ [Edit] [Pause] [View History]                │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Schedule 2: Weekly Content Calendar          │   │
│ │ Status: ✅ ACTIVE                            │   │
│ │ Frequency: Every Sunday @ 7:00 PM            │   │
│ │ Last Run: May 4 (generated 5-day plan)       │   │
│ │ Next Run: May 11                             │   │
│ │                                              │   │
│ │ Rule: Analyze analytics from past week       │   │
│ │       Plan content for upcoming week         │   │
│ │       Auto-generate scripts for Mon-Fri      │   │
│ │       Assign to: Creator mode                │   │
│ │       Max spend: $50.00                      │   │
│ │                                              │   │
│ │ [Edit] [Pause] [View History]                │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Schedule 3: Sunday Sovereign Briefing         │   │
│ │ Status: ✅ ACTIVE                            │   │
│ │ Frequency: Every Sunday @ 6:00 PM            │   │
│ │ Last Run: May 4 (sent briefing email)        │   │
│ │ Next Run: May 11                             │   │
│ │                                              │   │
│ │ Rule: Generate weekly briefing (as seen in   │   │
│ │       Screen 15), email to Founder           │   │
│ │       Include metrics, insights, costs       │   │
│ │                                              │   │
│ │ [Edit] [Pause] [View History]                │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ Schedule 4: Failed Job Recovery (Replay)     │   │
│ │ Status: ✅ ACTIVE                            │   │
│ │ Frequency: Every 6 hours                     │   │
│ │ Last Run: Today 12:00 (replayed 1 failed job)│   │
│ │ Next Run: Today 18:00                        │   │
│ │                                              │   │
│ │ Rule: Find dossiers with status=ERROR        │   │
│ │       Auto-replay failed workflow stage      │   │
│ │       Max 3 retry attempts per job            │   │
│ │       Escalate if still failing              │   │
│ │                                              │   │
│ │ [Edit] [Pause] [View History]                │   │
│ │                                              │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [Create New Schedule]                              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Features**:
- List all active schedules
- Schedule status (active, paused, error)
- Frequency & next run time
- Last run details (success/failure, items processed)
- Edit, pause, view history
- Create new schedule (modal with rule builder)

---

### Screen 17: Analytics Dashboard & Feedback Loop

**Purpose**: Aggregate analytics from all published content, drive insights

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ Analytics Dashboard — Multi-Channel Performance      │
├─────────────────────────────────────────────────────┤
│ Time Range: [Last 7 Days v] [Channels: All v]      │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ OVERALL METRICS                              │   │
│ │ Total Views:       18,234 (↑ 12% vs prev)   │   │
│ │ Total Engagement:  14,567 (↑ 18% vs prev)   │   │
│ │ Avg. Engagement %: 3.2% (↑ 0.5 pts)         │   │
│ │ Total Shares:      2,345 (↑ 25% vs prev)    │   │
│ │                                              │   │
│ │ Est. Audience Reached: 45,600 unique users  │   │
│ │ Est. New Followers: 892 (↑ 8%)               │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ BY CHANNEL PERFORMANCE                       │   │
│ │ ╔─────────┬────────┬────────┬──────────────╗ │   │
│ │ ║Channel  ║ Views  ║ Engage ║ Avg %        ║ │   │
│ │ ╠─────────┼────────┼────────┼──────────────╣ │   │
│ │ ║YouTube  ║ 12,340 ║  2,840 ║ 2.3% (low)   ║ │   │
│ │ ║Instagram║  4,200 ║  2,100 ║ 5.0% (high)  ║ │   │
│ │ ║LinkedIn ║  1,200 ║    450 ║ 3.8% (med)   ║ │   │
│ │ ║Blog     ║   400  ║    150 ║ 3.8% (med)   ║ │   │
│ │ ║TikTok   ║     94 ║     27 ║ 2.9% (low)   ║ │   │
│ │ ║Podcast  ║     0  ║      0 ║ 0.0% (new)   ║ │   │
│ │ ╚─────────╩────────╩────────╩──────────────╝ │   │
│ │                                              │   │
│ │ Note: Instagram Reels strongest performer   │   │
│ │       YouTube has largest audience but      │   │
│ │       lower engagement. Investigate format  │   │
│ │       or timing issues.                      │   │
│ │                                              │   │
│ │ Recommendation: Repurpose top Instagram     │   │
│ │ content to YouTube long-form (add context)  │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ ┌──────────────────────────────────────────────┐   │
│ │ TOP PERFORMING CONTENT (Last 7 Days)         │   │
│ │ 1. "AI Tips for Creators" (Instagram Reel)   │   │
│ │    Views: 9,200 | Likes: 2,100 (22.8%)       │   │
│ │                                              │   │
│ │ 2. "Machine Learning 101" (YouTube Short)    │   │
│ │    Views: 4,230 | Likes: 340 (8.0%)          │   │
│ │                                              │   │
│ │ 3. "Cloud Computing Trends" (LinkedIn)       │   │
│ │    Views: 1,200 | Comments: 87 (7.3%)        │   │
│ │                                              │   │
│ │ Insight: Shorter, actionable content          │   │
│ │ (tips, trends) outperforms deep dives.       │   │
│ │ Suggest: More "quick tips" series.            │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ Feedback Loop (Auto-suggestions to Creator):       │
│ ┌──────────────────────────────────────────────┐   │
│ │ Based on analytics, next week we suggest:   │   │
│ │                                              │   │
│ │ ✓ Create more Instagram Reels (high ROI)    │   │
│ │ ✓ Focus on "tips & tricks" format           │   │
│ │ ✓ Post Instagram at 7-8 PM (peak time)      │   │
│ │ ✗ Reduce YouTube long-form (low engagement) │   │
│ │ ✗ Avoid overly technical topics             │   │
│ │                                              │   │
│ │ [Implement Suggestions] [Dismiss] [Snooze] │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [Export as PDF] [Share with Team] [Download Data]  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Functionality**:
- Real-time metrics from YouTube, Instagram, LinkedIn, TikTok APIs
- Channel comparison (which channels perform best)
- Top-performing content analysis
- Engagement trends (7-day, 30-day, all-time)
- Auto-generated suggestions (based on performance data)
- Export/share analytics

---

## PART 3: MULTI-CHANNEL ORCHESTRATION SYSTEM

### 3.1 Multi-Channel Content Strategy

**Current State (PROD-01/02/03)**:
- Single dossier output (script, voice, images, etc.)
- User manually repurposes for each channel

**Future State (PROD-06)**:
- **Single dossier → Multi-channel outputs** (automatic format conversion)
- Platform-specific metadata (titles, descriptions, hashtags)
- Approval workflow per channel
- Scheduled publishing across all channels
- Analytics aggregation from all channels

### 3.2 Supported Channels (PROD-06)

| Channel | Supported Formats | Approval Gate | Publishing | Analytics |
|---------|-------------------|---|---|---|
| **YouTube** | Long-form (10-60 min) | Founder | API upload | View count, engagement, audience retention |
| **YouTube Shorts** | Short-form (15-60 sec) | Founder | API upload | View count, engagement rate |
| **Instagram Reels** | Short-form (15-90 sec) | Founder | Manual or API | Views, likes, shares, comments |
| **Instagram Feed** | Static images + captions | Founder | Manual or API | Likes, comments, saves |
| **TikTok** | Short-form (15-180 sec) | Founder | Manual upload (API limited) | Views, engagement, shares, follower growth |
| **LinkedIn** | Articles + text posts | Founder | API post | Views, engagements, shares, followers |
| **X/Twitter** | Text + images + links | Founder | API tweet | Impressions, engagements, retweets |
| **Blog** | Long-form articles + images | Founder | API post (WordPress, Medium) | Page views, scroll depth, time on page |
| **Newsletter** | Email + HTML | Founder | Email service API | Open rate, click-through rate, unsubscribe |
| **Podcast** | Audio episodes + metadata | Founder | Podcast hosting API | Downloads, listener retention, reviews |

### 3.3 Automatic Format Conversion

**Example: YouTube Script → Multi-Channel**

```
Input: Dossier-005 (1,850-word YouTube script)
       with voice (4:20 audio) and images

Output:
├─ YouTube Long-Form (15 min)
│  └─ Script: full 1,850 words
│  └─ Visuals: Ken Burns effect over images
│  └─ Audio: ElevenLabs voice
│  └─ Title: "AI Trends in 2026"
│  └─ Description: Full script + links + timestamps
│  └─ Tags: [AI, trends, 2026, LLMs, agents, ...]
│
├─ YouTube Shorts (60 sec) [TRUNCATED]
│  └─ Script: 100-150 words (hook + key point + CTA)
│  └─ Visuals: B-roll clips + text overlays
│  └─ Audio: Faster delivery speed (1.25x)
│  └─ Title: "Top AI Trends 2026 #Shorts"
│
├─ Instagram Reel (60 sec) [ADAPTED]
│  └─ Script: 80-100 words (even shorter, trendy)
│  └─ Visuals: Vertical format (9:16)
│  └─ Audio: Trending music underneath + voice
│  └─ Caption: Emoji-heavy, hashtags for reach
│  └─ Hashtags: #AI #TechTrends #2026 #Innovation
│
├─ TikTok (60 sec) [ADAPTED]
│  └─ Script: 60-80 words (TikTok style, snappier)
│  └─ Visuals: Vertical (9:16), trending effects
│  └─ Audio: Popular TikTok sound + voice
│  └─ Caption: Hook + CTA (max 150 chars)
│  └─ Hashtags: Trending + niche + creator
│
├─ LinkedIn Article [ADAPTED]
│  └─ Script: 800-1,000 words (professional tone)
│  └─ Format: Markdown with sections, bold highlights
│  └─ Images: 1-2 key visuals (professional style)
│  └─ Subtitle: Hook sentence
│  └─ CTA: "Agree? Disagree? Comment below"
│
├─ Blog Post [ADAPTED]
│  └─ Script: Full 1,850 words
│  └─ Format: HTML with h2, h3, bullet lists
│  └─ Images: 3-5 relevant images (SEO-optimized)
│  └─ Meta Title: "AI Trends 2026: What You Need to Know"
│  └─ Meta Description: 160-char SEO snippet
│  └─ Internal Links: Link to related posts
│
├─ Podcast Episode [NEW]
│  └─ Script: 1,850 words as monologue + intro/outro
│  └─ Audio: Original voice OR add intro music
│  └─ Duration: 10-15 minutes (standard for solo podcasts)
│  └─ Metadata: Title, description, cover art, show notes
│  └─ Platform: Spotify, Apple Podcasts, RSS feed
│
├─ Newsletter [ADAPTED]
│  └─ Script: 300-400 words (summary + key points)
│  └─ Format: Email HTML template
│  └─ Images: Hero image + 1-2 inline images
│  └─ CTA: "Read full article" link to blog
│  └─ Subject: Engaging teaser (best CTR subject lines)
│
└─ X/Twitter Thread [CONDENSED]
   └─ Tweet 1 (Hook): "Did you know? AI trends in 2026..."
   └─ Tweet 2: "1. Large Language Models are..."
   └─ Tweet 3: "2. Autonomous Agents will..."
   └─ Tweet 4: "3. Enterprise AI adoption..."
   └─ Tweet 5: "Your thoughts? Reply below!"
   └─ Images: 1 image per tweet (GIF or static)
```

### 3.4 Platform-Specific Metadata

**YouTube Long-Form**:
```yaml
title: "AI Trends in 2026 — What You Need to Know"
description: |
  Discover the latest AI trends shaping 2026:
  
  ⏰ Timestamps:
  0:00 - Intro
  0:45 - Large Language Models
  5:30 - Autonomous Agents
  8:45 - Enterprise Adoption
  12:00 - Conclusion
  
  📚 Resources:
  - https://example.com/ai-trends-2026
  - https://arxiv.org/... (research paper)
  
  👉 Subscribe for more AI insights!
  
  #AI #Trends #2026 #LLM #Agents

tags:
  - AI
  - Trends
  - Machine Learning
  - Large Language Models
  - Agents
  - 2026
  - Technology
  
category: "Science & Technology"
thumbnail_url: "path_to_hero_image"
privacy_status: "public"
made_for_kids: false
```

**Instagram Reel**:
```yaml
caption: "The 3 biggest AI trends you need to know about in 2026 🚀

✨ Swipe to learn:
1️⃣ LLMs are getting smarter
2️⃣ AI agents are autonomous
3️⃣ Enterprise AI adoption

Which trend excites you most? Comment below! 👇

#AI #Trends #Technology #Innovation #MachineLearning"

hashtags:
  - #AI
  - #Trends
  - #TechTrends2026
  - #MachineLearning
  - #Innovation
  - #FYP
  - #ForYou
  - #Explore

location: null
alt_text: "3 AI trends for 2026 visual infographic"
audio_credit: "Trending audio track name"
```

**LinkedIn Article**:
```yaml
title: "The 3 AI Trends Shaping Enterprise in 2026"
subtitle: "From LLMs to autonomous agents: what you need to know"
content: |
  **Introduction**
  
  AI is evolving rapidly. Here are three trends every enterprise leader should watch...
  
  **1. Large Language Models at Scale**
  
  [Body content...]
  
  **2. Autonomous AI Agents**
  
  [Body content...]
  
  **3. Enterprise Adoption Acceleration**
  
  [Body content...]
  
  **Conclusion**
  
  [Closing thoughts...]

featured_image_url: "path_to_hero_image"
visibility: "public"
allow_comments: true
notify_followers: true
```

### 3.5 Multi-Channel Approval Workflow

**Current (PROD-01/02/03)**:
- Single approval: Founder approves script → Published once

**Future (PROD-06)**:
```
Dossier Created
  ↓
Format Conversion (1 script → 10 channel variants)
  ↓
Channel Approval Gate:
  ├─ YouTube: Founder approves (specific notes for YouTube)
  ├─ Instagram: Founder approves (Reel-specific feedback)
  ├─ LinkedIn: Founder approves (tone check)
  ├─ TikTok: Founder approves (hook too slow?)
  ├─ Blog: Founder approves (SEO keywords?)
  ├─ Podcast: Founder approves (audio quality OK?)
  ├─ Newsletter: Founder approves (CTA clear?)
  ├─ X/Twitter: Founder approves (thread coherent?)
  └─ [Others]: Automatic approval or skip
  
Channel Publishing:
  ├─ YouTube: Scheduled for May 5 @ 9:00 AM (peak time)
  ├─ Instagram: Scheduled for May 5 @ 7:00 PM (max reach)
  ├─ LinkedIn: Scheduled for May 6 @ 9:00 AM (weekday)
  ├─ TikTok: Scheduled for May 5 @ 6:00 PM (trending time)
  └─ Blog: Published immediately (evergreen content)

Post-Publishing Monitoring:
  ├─ Collect analytics from each platform (hourly)
  ├─ Generate insights (which channels performing best?)
  ├─ Feedback to Creator (next week, focus on X channel)
  └─ Cost tracking (per-platform publishing costs)
```

---

## PART 4: 11 AUTOMATED SCHEDULER MODES

### 4.1 Scheduler Mode 1: Daily Topic Hunt

**Purpose**: Automatically discover trending topics and create dossiers

**Trigger**: Every day @ 8:00 AM  
**Process**:
1. Query APIs: Google Trends, Twitter Trends, Reddit Hot Posts, HackerNews
2. Filter by category (AI, Tech, Business, etc.)
3. Rank by potential engagement
4. Create dossier for top N topics (configurable: 1-5)
5. Auto-execute WF-100 (topic intelligence)
6. Notify Creator: "New dossiers created, awaiting your approval"

**Configuration**:
```yaml
scheduler_mode: daily_topic_hunt
enabled: true
frequency: "0 8 * * *"  # 8 AM daily
config:
  apis:
    - google_trends
    - twitter_trends  
    - reddit_hot
    - hackernews_top
  filters:
    category: ["AI", "tech"]
    min_engagement_score: 0.5
  auto_execute:
    - WF-100  # Topic intelligence
  output:
    create_dossiers: true
    num_topics: 3  # Top 3 topics
    max_budget_per_dossier: $10.00
    total_daily_budget: $30.00
  notify:
    creator: true
    founder: false
```

**Example Output (Auto-Generated Dossier)**:
```
Dossier-001: "OpenAI Releases GPT-5 Rumors" (trending #1)
  Status: TOPIC_RESEARCH_RUNNING (WF-100 executing)
  Budget: $10.00
  ETA: 2 minutes

Dossier-002: "Quantum Computing Breakthrough at IBM" (trending #2)
  Status: TOPIC_RESEARCH_RUNNING (WF-100 executing)
  Budget: $10.00
  ETA: 2 minutes

Dossier-003: "EU AI Regulation Updates" (trending #3)
  Status: TOPIC_RESEARCH_RUNNING (WF-100 executing)
  Budget: $10.00
  ETA: 2 minutes

→ Creator: Review results in 2 min, approve to continue to WF-200
```

### 4.2 Scheduler Mode 2: Daily/Weekly Content Calendar

**Purpose**: Plan week's content based on analytics and strategy

**Trigger**: Every Sunday @ 7:00 PM  
**Process**:
1. Analyze past week's analytics (views, engagement by channel)
2. Identify top-performing content formats/topics
3. Plan next week's content calendar (5 dossiers)
4. Auto-generate scripts for Mon-Fri
5. Schedule publishing times (optimal by channel)
6. Notify Creator/Founder: "Next week's content plan ready"

**Configuration**:
```yaml
scheduler_mode: weekly_content_calendar
enabled: true
frequency: "0 19 * * 0"  # Sunday 7 PM
config:
  analytics_window: 7  # days
  plan_horizon: 7     # days ahead
  content_strategy:
    mix:
      long_form: 30%    # YouTube long-form
      short_form: 40%   # Shorts, Reels, TikTok
      articles: 20%     # Blog, LinkedIn
      audio: 10%        # Podcast
  auto_execute:
    - WF-100  # Topic intelligence
    - WF-200  # Script generation (Mon-Fri scripts)
  output:
    create_dossiers: 5
    max_budget: $50.00
    publishing_schedule: true
    notify_founder: true
```

**Example Output**:
```
Monday 05/08: "Top 5 AI News This Week"
  Format: YouTube Short (60 sec) + TikTok
  Topic: Aggregated trending topics
  Budget: $8.00
  Publishing: Mon 9:00 AM YouTube, Mon 6:00 PM TikTok

Tuesday 05/09: "Machine Learning for Beginners"
  Format: Blog article + LinkedIn
  Topic: Educational deep-dive
  Budget: $5.00
  Publishing: Tue 10:00 AM Blog, Tue 9:00 AM LinkedIn

Wednesday 05/10: "The Future of AI Agents"
  Format: YouTube Long-form (15 min) + Podcast
  Topic: Analysis + predictions
  Budget: $15.00
  Publishing: Wed 9:00 AM YouTube, Wed 5:00 PM Podcast

Thursday 05/11: "AI Tools You Should Know"
  Format: Instagram Reel + TikTok + Blog
  Topic: Practical tools roundup
  Budget: $10.00
  Publishing: Thu 7:00 PM Instagram, Thu 6:00 PM TikTok, Thu 10:00 AM Blog

Friday 05/12: "Q&A: Your AI Questions Answered"
  Format: YouTube Short (community engagement)
  Topic: Answer viewer comments
  Budget: $3.00
  Publishing: Fri 9:00 AM YouTube

Total Budget: $41.00 (within $50 weekly limit)
→ Creator: Review plan, adjust topics/budget if needed, approve to execute
```

### 4.3 Scheduler Mode 3: Batch Generation (Monthly)

**Purpose**: Create 20-30 dossiers in one batch (monthly content batch)

**Trigger**: First Monday of month @ 10:00 AM  
**Process**:
1. Suggest 20-30 topics for the month
2. Create all dossiers simultaneously
3. Execute WF-100 + WF-200 in parallel (batch execution)
4. Generate all scripts in 1-2 hours
5. Queue for Founder approval
6. Schedule publishing throughout month

**Configuration**:
```yaml
scheduler_mode: batch_generation_monthly
enabled: true
frequency: "0 10 ? * MON#1"  # First Monday
config:
  batch_size: 25
  auto_execute:
    - WF-100  # In parallel
    - WF-200  # In parallel
  max_budget: $300.00
  output:
    create_dossiers: 25
    expected_duration_minutes: 90
    notify_founder: true
```

### 4.4 Scheduler Mode 4: Weekly Backup & Archive

**Purpose**: Backup all dossiers, archive old data

**Trigger**: Every Sunday @ 11:00 PM  
**Process**:
1. Zip all dossiers created this week
2. Backup to cloud storage (S3, Google Drive, OneDrive)
3. Archive dossiers older than 90 days
4. Compress old dossiers (remove audit trail, keep outputs)
5. Verify backup integrity
6. Notify Founder: "Backup complete, 0 errors"

**Configuration**:
```yaml
scheduler_mode: weekly_backup_archive
enabled: true
frequency: "0 23 * * 0"  # Sunday 11 PM
config:
  backup_destination: "s3://shadow-creator-backups/"
  archive_dossiers_older_than_days: 90
  verify_backup: true
  notify_founder: true
```

### 4.5 Scheduler Mode 5: Sunday Sovereign Briefing

**Purpose**: Generate executive briefing for Founder

**Trigger**: Every Sunday @ 6:00 PM  
**Process**:
1. Aggregate all metrics from past week
2. Generate brief report (see Screen 15: Weekly Briefing)
3. Include insights & recommendations
4. Email to Founder with PDF export
5. Post to internal dashboard

**Configuration**:
```yaml
scheduler_mode: sunday_sovereign_briefing
enabled: true
frequency: "0 18 * * 0"  # Sunday 6 PM
config:
  metrics:
    - views_by_channel
    - engagement_rates
    - cost_breakdown
    - top_content
    - trending_topics
  email:
    to: founder@example.com
    format: HTML + PDF attachment
    subject: "Weekly Briefing: Shadow Creator OS Metrics"
  include_recommendations: true
```

### 4.6 Scheduler Mode 6: Alert Digest & Error Summary

**Purpose**: Daily digest of errors and alerts

**Trigger**: Every morning @ 9:00 AM  
**Process**:
1. Collect all alerts from past 24 hours
2. Group by severity (critical, warning, info)
3. Summarize with suggested actions
4. Email to Operator/Founder
5. Post to Alert Center

**Configuration**:
```yaml
scheduler_mode: alert_digest
enabled: true
frequency: "0 9 * * *"  # 9 AM daily
config:
  time_window_hours: 24
  include:
    - critical_errors
    - rate_limits
    - cost_overages
    - provider_timeouts
  email:
    to: [founder, operator]
    include_suggestions: true
```

### 4.7 Scheduler Mode 7: Stuck Dossier Detector

**Purpose**: Find dossiers stuck in workflows, auto-replay or escalate

**Trigger**: Every 2 hours  
**Process**:
1. Find dossiers with status unchanged for >30 min
2. Check if WF is still executing or actually stuck
3. If stuck: Auto-replay with increased timeout
4. If replay fails: Escalate to Founder with error details
5. Log all checks to audit trail

**Configuration**:
```yaml
scheduler_mode: stuck_dossier_detector
enabled: true
frequency: "0 */2 * * *"  # Every 2 hours
config:
  stuck_threshold_minutes: 30
  auto_retry_enabled: true
  max_retry_attempts: 2
  escalate_on_failure: true
  notify: founder
```

### 4.8 Scheduler Mode 8: Provider Cost Monitor

**Purpose**: Track spending, warn of overages, enforce budgets

**Trigger**: Every hour  
**Process**:
1. Sum all dossier costs for the day
2. Project daily total vs budget
3. If >80% of budget: Warn Founder
4. If budget exceeded: Block new dossier creation
5. Track monthly trend
6. Suggest cost optimization (use Ollama vs GPT-4, etc.)

**Configuration**:
```yaml
scheduler_mode: provider_cost_monitor
enabled: true
frequency: "0 * * * *"  # Hourly
config:
  daily_budget: $50.00
  warning_threshold: 0.8  # 80%
  hard_limit: 1.0         # 100% = block
  track_monthly: true
  notifications:
    - at_80_percent
    - at_100_percent
    - daily_summary
```

### 4.9 Scheduler Mode 9: Replay Failed Jobs

**Purpose**: Automatically retry failed dossiers

**Trigger**: Every 30 minutes  
**Process**:
1. Find dossiers with status=ERROR
2. Determine root cause (timeout, rate limit, etc.)
3. Auto-replay with adjusted parameters
4. Max 3 attempts per dossier
5. If still failing: Escalate to Founder

**Configuration**:
```yaml
scheduler_mode: replay_failed_jobs
enabled: true
frequency: "*/30 * * * *"  # Every 30 min
config:
  max_attempts: 3
  backoff_strategy: exponential  # Wait longer on each retry
  auto_adjust:
    - increase_timeout_on_timeout
    - wait_longer_on_rate_limit
    - fallback_to_ollama_if_provider_error
  escalate_after_max_attempts: true
```

### 4.10 Scheduler Mode 10: Recurring Channel Plans

**Purpose**: Automatically publish to channels on recurring schedule

**Trigger**: Configured per channel (e.g., "YouTube Mon/Wed/Fri @ 9 AM")  
**Process**:
1. Check if publishing slot has scheduled content
2. If approved dossier exists: Publish automatically
3. If no dossier: Create placeholder or skip
4. Log publication to audit trail
5. Monitor for errors (upload failures, etc.)

**Configuration**:
```yaml
scheduler_mode: recurring_channel_plans
enabled: true
channels:
  youtube:
    frequency: "0 9 ? * MON,WED,FRI"  # Mon/Wed/Fri @ 9 AM
    auto_publish_approved: true
    fallback: "publish_template_content"
  instagram:
    frequency: "0 19 ? * MON,WED,FRI"  # Mon/Wed/Fri @ 7 PM
    auto_publish_approved: true
    fallback: "skip_if_no_content"
  blog:
    frequency: "0 10 ? * MON,THU"  # Mon/Thu @ 10 AM
    auto_publish_approved: true
    fallback: "queue_for_manual_review"
```

### 4.11 Scheduler Mode 11: Weekly Analytics Sync

**Purpose**: Pull analytics from all channels, update dossier records, feed insights to Creator

**Trigger**: Every Monday @ 12:00 PM  
**Process**:
1. Pull analytics from YouTube, Instagram, LinkedIn, TikTok, Blog, Podcast APIs
2. Match content to dossiers (by URL, title, upload date)
3. Update dossier records with final metrics
4. Aggregate insights (what worked, what didn't)
5. Generate suggestions for next content (see Screen 17)
6. Email Creator with recommendations

**Configuration**:
```yaml
scheduler_mode: weekly_analytics_sync
enabled: true
frequency: "0 12 ? * MON"  # Monday noon
config:
  platforms:
    - youtube
    - youtube_shorts
    - instagram
    - tiktok
    - linkedin
    - blog
    - podcast
  metrics:
    - views
    - engagement
    - shares
    - followers_gained
    - avg_watch_time
  match_dossier: true  # Link analytics back to original dossier
  generate_suggestions: true
  notify_creator: true
```

---

## PART 5: ARCHITECTURE ENFORCEMENT RULE (Critical)

### Golden Rule: GUI/Scheduler → Operator API Only

**This rule is immutable. No exceptions.**

```
User (GUI)
  ↓
[GUI Layer - 17 Screens]
  ├─ Create Content → Task Builder
  ├─ Monitor → Dashboard, Alerts, Analytics
  ├─ Approve → Approval Screen
  ├─ Schedule → Scheduler Console
  ├─ Publish → Channel Calendar
  └─ All screens MUST route to Operator API
  ↓
[Operator API - localhost:5050]
  ├─ POST /operator/new-content-job
  ├─ GET  /operator/dossier/:id
  ├─ POST /operator/approve/:id
  ├─ POST /operator/remodify/:id
  ├─ POST /operator/replay/:id
  ├─ POST /operator/dossier/:id/mutate
  └─ All requests validated, cost-gated, logged
  ↓
[n8n Workflow Registry]
  ├─ WF-001 (Dossier Create)
  ├─ WF-100 (Topic Intelligence)
  ├─ WF-200 (Script Generation)
  ├─ WF-300-600 (Media generation)
  ├─ WF-660 (Publishing)
  └─ WF-900+ (System handlers)
  ↓
[Dossier & Packet System]
  ├─ All mutations to dossier.json
  ├─ All actions to audit_trail.json
  ├─ All outputs to packets/ folder
  └─ All costs tracked in cost_tracking

NEVER ALLOWED:
✗ GUI directly calls n8n webhook (bypass Operator API)
✗ GUI directly calls provider API (ElevenLabs, HeyGen, etc.)
✗ GUI directly modifies dossier file (filesystem)
✗ Scheduler directly calls provider (must use Operator API)
✗ Scheduler directly writes dossier (must use Operator API)

REQUIRED ARCHITECTURE:
✓ GUI Layer (user-facing)
  ↓
✓ Operator API (validation, cost gates, audit)
  ↓
✓ n8n Workflows (execution orchestration)
  ↓
✓ Dossier System (persistent state, audit trail)

CONSEQUENCE OF VIOLATION:
If any GUI screen or Scheduler directly calls a provider or 
modifies dossier files, all Founder approval gates are 
bypassed → cost overages, audit trail loss, compliance failure.

This rule must be enforced at architecture level (URL routing,
API gateway, code review).
```

---

## PART 6: SUCCESS CRITERIA FOR PROD-06

**GUI + Scheduler + Multi-Channel system is COMPLETE when**:

✅ All 17 GUI screens functional and tested
✅ All 11 Scheduler modes operating without errors
✅ Multi-channel format conversion working (1 dossier → 10 outputs)
✅ Channel-specific approval workflow tested (per-platform approvals)
✅ Automatic publishing to YouTube, Instagram, LinkedIn, TikTok, Blog, Podcast, Newsletter
✅ Real-time analytics aggregation from all channels
✅ Weekly briefing auto-generated with insights
✅ Cost monitoring enforcing daily/weekly budgets
✅ Zero direct GUI→Provider calls (Routing Law enforced)
✅ Audit trail complete for all automated actions
✅ Founder sign-off: "This is a complete content creation + publishing platform"

---

**Status**: 📋 DESIGN_ONLY — GUI/Scheduler not yet implemented  
**Target Release**: PROD-06 (Q3-Q4 2026 estimate, after PROD-03/04/05 complete)  
**Tech Stack**: React.js (frontend), Node.js/Express (backend), PostgreSQL (long-term scheduling state)  
**Founder Authority**: Required for scheduler policy configuration and approval gate settings  

---

