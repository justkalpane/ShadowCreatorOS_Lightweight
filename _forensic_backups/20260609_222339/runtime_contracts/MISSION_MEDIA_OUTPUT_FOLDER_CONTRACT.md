# Mission Media Output Folder Contract

## Purpose

When media generation is approved, the mission must use one dedicated mission
folder that keeps required files together and prevents leftover clutter from
polluting the repo or the external media workspace.

This contract does not override chat-only mode. It applies only when the task
has moved beyond chat-only planning into approved repo-write or approved media
generation support.

It must not be invoked as a file-creation instruction during a Visual Media
Plan. A generator draft may declare this bundle structure in chat, but actual
folder, document, JSON, TXT, packet, or media creation is allowed only after an
explicit repo-write or media-generation approval for that stage.

## Mission Root

Default mission root:

```text
outputs/missions/<mission_id>/
```

## Required Mission Bundle

Every mission media output bundle must declare:

```text
mission_root=
consolidated_plan_doc=
scene_packets_dir=
voice_dir=
music_dir=
sfx_dir=
images_dir=
broll_dir=
aroll_dir=
hyperframes_dir=
davinci_dir=
proofs_dir=
supporting_image_generation_txt=
supporting_voice_generation_txt=
supporting_music_sfx_txt=
supporting_editing_txt=
supporting_hyperframes_txt=
cleanup_policy=
```

## Consolidated Plan Document Law

One consolidated human-readable plan document must sit at the mission root when
repo-write is approved for execution support.

It may be a Word document or another approved human-readable master document,
but it must act as the operator-facing consolidated reference for the mission.

## Support File Law

The support files must be cleanly separated by lane so that agents and humans
can execute the workflow without re-parsing one giant mixed packet.

Expected support files:

- image generation support
- voice generation support
- music and SFX support
- editing support
- HyperFrames support
- packet JSON support

## Output Separation Law

Rendered or generated files must be stored under the mission bundle in their
own lane-specific folders rather than dumped into one mixed directory.

Required separation:

- `voice/`
- `music/`
- `sfx/`
- `images/`
- `broll/`
- `aroll/`
- `hyperframes/`
- `davinci/`
- `proofs/`

## Cleanup Law

Temporary, duplicate, abandoned, or intermediate scratch files may exist while
the task is active, but the final mission state should keep only what is
required for:

- execution
- proof
- re-entry
- later editing

Required cleanup policy value:

```text
cleanup_policy=keep_required_delete_temporary
```

If the task completes successfully, unnecessary temporary folders should be
deleted or archived outside the final required mission bundle.

## Honesty Boundary

Declaring a mission bundle plan is not the same as creating those files.
Do not claim output folders or generated assets exist unless they were actually
created and can be referenced.
