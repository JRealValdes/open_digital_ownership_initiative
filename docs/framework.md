# Digital Ownership Framework

**Version:** 1.1.0  
**Status:** Community proposal  
**Scope:** Video games (principles may later extend to other digital goods)  
**License:** [CC BY 4.0](../LICENSE)

A proposal for durable consumer ownership of video games in a primarily
digital distribution world—without discarding digital convenience, and
without discarding physical ownership where it still adds value.

---

## 1. Purpose

Digital distribution is efficient, convenient, and increasingly the
default way players acquire games. That shift should not quietly replace
**ownership** with a temporary **licence to use** that depends on a
store, an account, or an online service remaining available.

This framework proposes a model in which:

1. Paying full purchase price for a game confers **ownership**, not merely
   permission.
2. Ownership is usable across multiple devices *within a platform*,
   recoverable after account problems, and transferable between people.
3. Digital and physical forms of ownership can coexist in **one library
   model**, rather than as incompatible tracks.
4. Security measures protect against ownership fraud without treating
   ordinary owners as adversaries.

This document is a **design proposal**, not a finished technical
standard, legal instrument, or product specification. Implementation
details (protocols, cryptography, commercial terms) are illustrative
unless marked as requirements of the model.

---

## 2. The problem

Under many current digital storefront models, a purchase typically
grants a **non-transferable licence** tied to a platform account. In
practice, that often means:

| Expectation from physical ownership | Common digital outcome |
|-------------------------------------|------------------------|
| You can keep the game indefinitely  | Access may end if the store or licence servers disappear |
| You can sell or give the game away  | Resale and gifting are usually forbidden or unsupported |
| You can lend the game               | Lending is usually unsupported |
| Possession is not the same as an account | Access is bound to an account; account loss can mean library loss |
| Offline play is normal              | Some titles require periodic or permanent online checks |

Physical media had flaws (disc rot, region locks, limited durability),
but it encoded a clear social and commercial fact: **the buyer held a
copy they could keep, move, and transfer**. Digital distribution removed
many of those frictions—and, too often, removed that fact as well.

The goal of this framework is not to reject digital distribution. It is
to keep digital advantages while restoring durable ownership rights.

---

## 3. Goals and non-goals

### 3.1 Goals

- Define what **ownership** means for digitally distributed games.
- Separate **ownership** from **account management**.
- Support **online-managed** and **offline-capable** ownership modes.
- Enable **transfer**, **lending**, and **preservation**.
- Allow **physical** and **digital** ownership to live in one coherent
  library model.
- Align incentives so platforms, publishers, and players can benefit
  from legitimate second-hand and lending activity.

### 3.2 Non-goals

- Eliminating all anti-fraud or anti-piracy measures.
- Mandating a single cryptographic technology or vendor.
- Replacing copyright law or regional consumer-protection statutes.
- Claiming that every form of access (subscriptions, rentals, free-to-play
  services) must be “ownership.” Those products can coexist; this
  framework addresses **purchase** that is marketed and priced as owning
  a game.
- **Cross-platform portability between competing ecosystems** (e.g. buying
  on one storefront and exercising the same owned copy on a rival
  platform). That remains commercially and technically distant today.
  This version targets multi-device use **within** a platform, plus the
  ownership rights in §4.1.

---

## 4. Core principles

### 4.1 Non-negotiable ownership rights

A purchase under this model must confer all of the following. Removing
any of them means the product is no longer “ownership” in the sense of
this framework:

1. **Ownership.** Paying the full purchase price creates ownership of
   that game copy—not a revocable storefront permission.
2. **Preservation.** The owner may keep and archive the game copy for
   personal preservation so that ownership remains meaningful over time,
   including beyond a single platform’s convenience layer.
3. **Lending.** The owner may lend the game copy for a defined period.
4. **Transfer.** The owner may give, sell, or otherwise permanently
   transfer the game copy; others may acquire it second-hand.

These four rights are the floor. Implementation details may vary;
hollowing them out is not compatible with the model.

### 4.2 Supporting design principles

1. **Ownership belongs to the person, not the account.** An account is a
   tool for managing ownership, not the ownership itself.
2. **Ownership must survive platform failure.** Store closure, service
   shutdown, or account disruption must not erase legally acquired
   ownership by default.
3. **Digital should strengthen ownership.** Convenience features
   (instant download, multi-device install, cloud saves) should not
   require surrendering the rights in §4.1.
4. **Security protects ownership.** Controls should prevent
   *duplication of ownership* and *unauthorised launch without an
   ownership proof*, not impose permanent surveillance or arbitrary
   limits on legitimate owners.
5. **Physical and digital are modes of the same right.** A player’s
   library may contain digitally managed titles and physically tokenised
   titles under one ownership model.

---

## 5. Key concepts

These definitions are used throughout the document. A fuller list lives
in [`glossary.md`](glossary.md).

| Term | Meaning |
|------|---------|
| **Game copy** | A specific instance of a game product that can be owned. Distinct from the abstract work (the copyrighted game as such). |
| **Ownership** | The durable right to possess, use, preserve, transfer, and lend a game copy, subject to the rules in this framework. |
| **Owner** | The natural person (or legal entity) who holds ownership of a game copy. |
| **Account** | A platform login used to *manage* ownership records. It is not ownership. |
| **Ownership record** | An authoritative entry stating who owns a given game copy and in which mode. |
| **Ownership mode** | How ownership is currently exercised: **Digital** or **Offline** (see §7). |
| **Ownership token** | A unique physical artefact that represents Offline Ownership of a game copy. |
| **Digital ownership credential** | Locally usable proof derived from a Digital Ownership record; used to authorise launch (including offline) without treating bare files as sufficient. |
| **Sealed content** | Game payload bound so unlock material derives from an ownership proof; suitable for preservation without enabling unowned play. |
| **Licence-to-use** | Permission to access a game without the transfer and longevity rights of ownership. Outside the purchase model this framework defines. |

**Important distinction:** game *files* (installers, binaries, assets) are
not ownership. Files can be copied; ownership cannot be honestly
duplicated. Ownership is represented by records and, in Offline mode, by
tokens. Under this model, **possession of files must not by itself
authorise launch**; play requires a valid ownership proof (see §12.3
and §13).

---

## 6. Ownership and accounts

### 6.1 Default relationship

By default, a platform account acts as the **custodian interface** for
the owner’s digital ownership records: purchases appear in the library,
installs are authorised, and transfers are initiated from that account.

### 6.2 Account loss must not equal ownership loss

Suspension, deletion, credential theft, or account replacement must not
automatically destroy ownership. The system should support **recovery of
ownership**, not recreation of a purchase.

Recovery may combine measures such as:

- identity verification
- recovery keys or backup credentials
- multi-factor authentication
- cooling-off / waiting periods
- manual review for high-risk cases

The exact mechanism is an implementation choice. The requirement of the
model is that **ownership remains recoverable** when the claimant can
credibly prove they are the owner.

### 6.3 One owner at a time

Except during a defined lending period (§10), each game copy has exactly
one owner. Transfer and lending change who may exercise play rights; they
must not create a second simultaneous owner of the same copy.

---

## 7. Ownership modes

Ownership exists in one of two modes. The owner may switch modes when
the model’s conditions are met. Switching is an **ownership event** and
may require network connectivity even if day-to-day play does not.

### 7.1 Digital Ownership (default)

Digital Ownership is the normal mode after an online purchase.

The owner may:

- install the game on multiple devices they control (§11)
- play offline for ordinary use, using a locally cached digital
  ownership credential (§12.3)
- keep personal backups of installers and game data for preservation (§12)
- move installations between personal devices

A network connection is required for **ownership events**, not for
routine play. Ownership events include:

- purchase
- sale or other permanent transfer
- lending start/end (when platform-mediated)
- conversion between Digital and Offline modes

Fraud detection should focus on abnormal patterns (e.g. industrial-scale
sharing), not on treating every owner as a presumed infringer.

### 7.2 Offline Ownership

Offline Ownership converts a digitally managed copy into a form that can
be held and transferred like physical media, while remaining part of the
same ownership model.

**How it works (conceptual model):**

1. The owner requests conversion from Digital to Offline mode.
2. The digital ownership record for that copy is **locked** so the title
   can no longer be played via the previous digital authorisations.
3. A unique **ownership token** is issued (or activated) to the owner.
4. The token is the portable proof of ownership for that copy.

Properties of the ownership token:

- **Unique** — one active token per game copy in Offline mode.
- **Non-duplicable as ownership** — copying the artefact must not create
  a second valid ownership.
- **Physically transferable** — giving the token away transfers the
  ability to claim ownership (subject to any activation/registration
  step the implementation defines).
- **Offline-capable** — once bound, play does not depend on a store
  remaining online for day-to-day use.

This is the modern analogue of a cartridge or disc **as a bearer of
ownership**, not necessarily as the sole storage medium for game files.
Game data may still be downloaded or installed digitally—preferably as
sealed content (§12.3); the token answers *who owns this copy* and is
required to authorise launch in Offline mode.

Conversion back to Digital Ownership is allowed: the token is
invalidated (or marked redeemed), and a digital ownership record is
restored to the owner’s account custody.

### 7.3 Choosing a mode

| Mode | Strengths | Trade-offs |
|------|-----------|------------|
| Digital | Instant management, easy multi-device, easy recovery workflows | Depends on custody systems and recovery processes |
| Offline | Works without ongoing store access; natural fit for physical sale and inheritance | Requires safeguarding the token; conversion steps needed to return to digital custody |

Neither mode is “more owned” than the other. Both express the same
underlying ownership of a game copy.

---

## 8. Unified library: digital and physical together

A player’s library under this model is a set of **owned game copies**,
each in Digital or Offline mode—not two disconnected catalogues.

Consequences:

1. **One library concept.** “What I own” is the set of ownership records
   and tokens, regardless of how the bits were obtained.
2. **Physical editions can participate.** A retail box / disc / cartridge
   can be treated as (or paired with) an ownership token for Offline
   mode, provided uniqueness and non-duplication of ownership are
   preserved. Legacy physical media may need a registration or bridging
   step; that is an adoption detail, not a change to the principle.
3. **Mode switching unifies behaviour.** Owners can move between digital
   convenience and physical transferability without buying the game
   twice.
4. **Retail and peer markets remain meaningful.** Second-hand shops and
   private sales continue to work for Offline tokens, while platforms
   can operate official digital transfer markets for Digital Ownership
   (§9).

The point is not nostalgia for plastic. It is continuity of rights:
digital distribution should not be a one-way door out of ownership.

---

## 9. Transfer and the second-hand market

Ownership implies the ability to transfer ownership of a game copy to
someone else.

### 9.1 Offline (physical) transfer

When a copy is in Offline mode, transfer follows possession of the
ownership token, similar to selling a disc today:

- private sales
- second-hand retailers
- gifts and inheritance

Implementations may require a one-time online activation when a new
holder first claims the token, as long as day-to-day play can remain
offline afterwards.

### 9.2 Digital transfer

Platforms may provide an official resale / transfer marketplace for
copies in Digital Ownership mode.

**Normative transfer flow:**

1. Seller requests transfer of a specific game copy.
2. The copy enters a **locked** state (no further installs/launches under
   the seller).
3. All of the seller’s authorised devices release that copy.
4. Ownership record is assigned to the buyer.
5. Buyer becomes the sole owner.

Lending (§10) uses a related lock/release pattern but is temporary and
reversible.

### 9.3 Incentives (illustrative)

A sustainable second-hand channel needs incentives for platforms and
rights-holders, not only for players. Revenue sharing on digital resale
is one approach. Example split (non-normative):

| Party | Share of resale price |
|-------|------------------------|
| Seller | 90% |
| Platform | 8% |
| Developer / publisher | 2% |

Other splits, fee caps, or time-gated first-sale rules are compatible
with this framework if they preserve the owner’s right to transfer.

---

## 10. Lending

An owner may lend a game copy for a defined period.

During an active loan:

- the borrower may play the copy
- the owner may not play that same copy
- ownership itself remains with the owner; only exercise of play rights
  is delegated

When the loan ends, play rights return to the owner automatically.

Lending may be implemented digitally (platform-mediated) or via Offline
mode (physical temporary transfer of the token). In both cases the rule
is the same: **one active player of a given owned copy at a time** under
ordinary use.

---

## 11. Multiple devices

Owners may install and play their games on multiple devices they
control **within the same platform ecosystem**. Moving a single owned
copy across competing storefronts or platform families is out of scope
for this version (see §3.2).

Perfect prevention of all simultaneous offline use across devices is
not realistically achievable without harming legitimate owners. For
*that* residual risk—an owner’s own devices used at the same time while
offline—this framework adopts a **trust-and-detect** posture:

- allow ordinary personal multi-device use
- detect and act on large-scale abuse (device farms, industrial sharing)
- avoid permanent always-online requirements and arbitrary install caps
  as the primary control mechanism

This posture applies to multi-device edge cases. It does **not** mean
implementations may rely on voluntary honesty for the basic rule that
unowned copies must not launch. Launch authorisation is a hard
requirement of §13.

Platforms may still use lightweight checks at ownership events, device
management tools, or abuse thresholds. Those measures must remain
proportionate to the goal of preventing ownership duplication.

---

## 12. Preservation

### 12.1 What owners may preserve

Owners may keep backups, archive installers, and maintain personal
library archives for games they own.

### 12.2 What preservation is not

Possessing files does not create ownership. Preservation without an
ownership record or valid offline token does not authorise redistributing
the game as if it were owned, and does not authorise play.

### 12.3 Backups must not equal a playable copy

Preservation and anti-fraud pull in the same direction when designed
correctly: owners should be able to archive what they own, and a shared
folder of game bits should not become a working game for someone who
lacks ownership.

**Requirement:** implementations must bind the right to *launch* a game
copy to a current ownership proof—either:

1. a **digital ownership credential** derived from a valid Digital
   Ownership record (which may be cached locally after an ownership
   event, so ordinary play can remain offline), or
2. a valid **ownership token** in Offline Ownership mode.

Absent one of those proofs, the copy must not be authorised to run.

**Recommended design:** treat distributable game payloads as **sealed
content** (for example encrypted or otherwise cryptographically bound)
whose usable keys or unlock material derive from the ownership proof.
Owners then back up sealed packages safely; the sensitive artefact is
the credential or token, not the raw playable tree in the clear.

Digital credentials used for offline launch may be device-bound or
otherwise limited so that copying the backup folder alone does not
transplant play rights. Mode conversion, transfer, and lending must
invalidate or re-issue credentials so that prior unlock material cannot
honestly keep working for a former holder.

Exact cryptography, packaging, and hardware choices are implementation
details (see §16). The normative rule is the binding: **no proof, no
launch**.

### 12.4 Preservation beyond platforms

Ownership should remain meaningful if:

- a storefront closes
- licence servers are shut down
- a company changes strategy or ceases operations

Practically, this pushes implementations toward:

- exportable ownership proofs
- offline mode as a durable escape hatch
- industry or third-party custody options for records when a platform
  exits

No proposal can force a bankrupt company to run servers forever. The
model’s requirement is that **ownership is designed to outlive a single
store’s convenience layer**, through records, tokens, and transferability
—not through hope that a service stays online.

---

## 13. Security posture

Security in this model has two clear objectives:

1. **Prevent dishonest multiplication of ownership** (two active owners
   of the same copy; play continuing after transfer or loan end).
2. **Prevent unauthorised launch** when no valid digital credential or
   offline token is present—including when someone only has preserved
   or shared game files.

These controls must still allow owners to exercise the rights in §4.1,
including offline ordinary play and personal preservation.

### 13.1 Threat model

| Threat | Posture under this framework |
|--------|------------------------------|
| Sharing backups / installers without ownership proof | **Mitigate:** sealed content + launch bound to credential or token (§12.3) |
| Claiming two owners of one copy via store/transfer abuse | **Prevent:** authoritative one-owner records; lock/release on transfer and lending |
| Industrial-scale device farms or credential trafficking | **Detect and act:** anomaly detection; proportionate enforcement |
| Determined reverse engineering / cracked clients | **Not promised:** no consumer scheme forever stops a motivated attacker; that failure mode does not excuse omitting the bindings above |

The model is not sustained by assuming people will be good. Casual
unauthorised play from bare files must fail by design. Residual risk
after that binding—especially sophisticated bypasses—is acknowledged
honestly rather than denied.

### 13.2 Compatible approaches (illustrative)

- sealed or encrypted game packages unlocked by ownership proofs
- locally cached, signed digital ownership credentials for offline launch
- cryptographic signatures over ownership records
- secure hardware or attestations for tokens
- unique ownership identifiers per game copy
- anomaly detection for resale, lending, and device farms

### 13.3 Approaches to avoid as defaults

- leaving game payloads freely runnable without any ownership check
- permanent online requirements for personal play
- treating every customer as a likely infringer
- opaque revocation with no recovery path
- restrictions that exist only to block second-hand markets

Security that destroys the rights it claims to protect is a design
failure under this framework. Security that relies only on voluntary
compliance for “files without proof must not play” is also a design
failure.

---

## 14. Roles and incentives

| Actor | Role in the model |
|-------|-------------------|
| **Player / owner** | Holds ownership; may use, preserve, lend, transfer, and switch modes. |
| **Platform** | Custodian of digital records; may operate transfer/lending markets; provides recovery. |
| **Publisher / developer** | Supplies the game; may receive a share of secondary-market activity; sets product policy within the model. |
| **Retailer** | May sell new copies and participate in physical/offline token markets. |
| **Archivists / museums** | Benefit from clearer preservation rights and surviving ownership proofs when platforms change. |

Adoption depends on making legitimate ownership **better for users** and
**viable for businesses**, not on demanding altruism alone.

---

## 15. Relationship to subscriptions and rentals

Subscriptions, rentals, and other temporary access products are
legitimate commercial offerings. This framework does not require them to
grant ownership.

It does require honesty of category:

- if a product is sold as a **purchase / buy / own**, it should follow
  ownership rules in this model
- if a product is temporary access, it should be presented as such

The consumer harm to avoid is **purchase-priced transactions that only
deliver revocable permission**.

---

## 16. Open questions

The following are intentionally unsettled in v1.1 and are good RFC
topics:

1. Concrete token formats and anti-cloning mechanisms.
2. Bridging legacy discs/cartridges into the unified library.
3. Minimum legal/consumer-protection hooks per jurisdiction.
4. Standard data formats for exporting ownership records.
5. Default lending durations and abuse limits.
6. How refunds interact with transfers and mode conversion.
7. Sealed-package formats and digital credential profiles that satisfy
   §12.3 without mandating always-online play.

---

## 17. Vision

Players should not have to choose between digital convenience and
meaningful ownership.

Digital technology should preserve what made physical ownership valuable
—keeping, lending, transferring, inheriting, and preserving a copy—while
adding what digital does best: instant delivery, easy reinstall, and
flexible device use.

If someone pays the full purchase price for a game, they should receive
**ownership of that game copy**. Digital distribution should make that
ownership stronger, not thinner.
