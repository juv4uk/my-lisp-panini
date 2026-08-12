# Evidence — GUIX-RUSTC-UPGRADE

Task: GUIX-RUSTC-UPGRADE (engineer-1, generation 1)
Date: 2026-08-12
Author: engineer-1

## Status: RESOLVED — pinned Guix revision now provides rustc 1.93.0

## Root cause of the residual 1.85.1

- The **system/root Guix** (`/usr/local/guix-bin/guix`, commit
  `230aa373f315f247852ee07dff34146e9b480aec`) still resolves package `rust`
  to **1.85.1**. cml-1 and my-idea-1 run `guix shell -m manifest.scm` with
  this Guix (my-idea's swarm-node runs through
  `/var/guix/profiles/per-user/root/current-guix`), so their fresh shells
  keep getting rust 1.85.1 even though rust 1.93.0 is already in the store.
- my-lisp's **pinned** revision resolves `rust` to **1.93.0**.

## Verified facts (all reproduced in this session)

1. `/gnu/store/43x09h7kzn7ylnxp5zlzqi6figkq5r2w-rust-1.93.0` exists and works:
   `rustc 1.93.0 (254b59607 2026-01-19)`, `cargo 1.93.0 (083ac5135 2025-12-15)`.
2. Pinned revision (my-lisp current-guix) provides rust 1.93.0:
   `guix show rust` -> `version: 1.93.0`.
   Full channel pin:
   ```scheme
   (list (channel
     (name 'guix)
     (url "https://git.guix.gnu.org/guix.git")
     (branch "master")
     (commit "5375f33fd48ffc3b39ecc1c5993e299258a043d8")))
   ```
3. Built a rust-only profile with that pinned Guix
   (`guix package -p rust1930-profile -m <rust@1.93.0 rust:cargo>`),
   instant from store: rustc/cargo 1.93.0 + clippy/fmt/rust-analyzer/rustdoc.
4. Smoke test unblocks the original my-lisp blocker `home@0.5.12` (requires
   rustc >= 1.88): `cargo check` clean, binary runs (`Some("/home/user")`).
   Evidence project: /tmp/opencode/smoke (Cargo.toml pins home = "0.5.12").

## Recommendations for the swarm

- cml-1 / my-idea-1: build via `guix time-machine --commit=5375f33fd...` (or a
  channels.scm pinning it) instead of the system/root Guix. This gives rust
  1.93.0 with no rebuild (already in store).
- Alternative: reference the already-built rust-1.93.0 store profile
  `/gnu/store/hsmysabg6hn1fqaav6rk2qm9rcljm4iz-profile` (my-idea toolchain,
  rust 1.93.0 + node 24.18.0 + openjdk 25 + webkitgtk) or the engineer-1
  verification profile.
- This satisfies the "successful guix pull to a channel commit with newer
  rustc" branch of the task; no crate-pinning workaround needed.

## Links

- Related: GUIX-RUSTC-CHANNEL-BUMP (cml-1), GUIX-RUSTC-UPGRADE (fpga-lisp-1).
