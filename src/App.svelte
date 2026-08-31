<script lang="ts">
  import { onMount } from 'svelte';

  type Agent = { name: string; state: string; progress: number };
  let morphology: 'atlas' | 'signal' = 'atlas';
  let active = 'Debate';
  let session = { topic: 'Port city climate adaptation', user: 'Mira Chen', agents: [] as Agent[] };
  let notice = 'Presentation A — Atlas';
  let thread: HTMLElement;
  let savedScroll = 0;
  let expanded = false;
  const messages = [
    ['Mira Chen', 'I need a decision framework for port-city adaptation that distinguishes near-term protection from long-term retreat.', 'human'],
    ['Research Agent', 'I mapped 18 coastal programs across Jakarta, Rotterdam, and New Orleans. The durable pattern is not a single barrier: it is a sequence of protection, accommodation, and managed transition.', 'research'],
    ['Critic Agent', 'Caution: the comparison hides governance differences. A plan that is technically elegant but displaces informal settlements is not an adaptation success.', 'critic'],
    ['Research Agent', 'The strongest evidence supports a 2030 / 2040 / 2050 horizon. Start with drainage and cooling corridors; reserve land now for water storage and voluntary relocation pathways.', 'research'],
    ['Mira Chen', 'What would make this legible to a mayor who has one election cycle to show progress?', 'human'],
    ['Synthesis Agent', 'Make the first act visible: a public heat-and-flood map, three demonstration blocks, and a commitment ledger. Pair each quick win with a protected corridor that remains useful under higher sea-level scenarios.', 'synthesis'],
    ['Critic Agent', 'The ledger needs a distribution column—who benefits, who is exposed, and who has a veto. Without that, “resilience” can become a cover for unequal redevelopment.', 'critic'],
    ['Synthesis Agent', 'Proposed decision: fund the three-block pilot now, establish a resident review table, and publish trigger thresholds for the transition from protection to accommodation.', 'synthesis']
  ];

  onMount(async () => {
    try { const r = await fetch('http://127.0.0.1:8011/api/session'); if (r.ok) session = await r.json(); } catch { /* rendered fallback remains truthful mock data */ }
  });

  function switchMorphology(next: 'atlas' | 'signal') {
    if (next === morphology) return;
    savedScroll = thread?.scrollTop ?? 0;
    morphology = next;
    notice = next === 'atlas' ? 'Presentation A — Atlas restored' : 'Presentation B — Signal activated';
    requestAnimationFrame(() => { if (thread) thread.scrollTop = savedScroll; });
  }
  function jumpToEnd() { thread?.scrollTo({ top: thread.scrollHeight, behavior: 'smooth' }); }
</script>

<svelte:head><title>MultiMind — Fieldroom</title><meta name="theme-color" content="#0d1215" /></svelte:head>

<main class:signal={morphology === 'signal'} class="shell">
  <div class="grain"></div><div class="sun"></div>
  <header class="topbar">
    <a class="mark" href="/" aria-label="MultiMind home"><i></i><span>MULTI<br/>MIND</span></a>
    <div class="project"><small>FIELDROOM / 07</small><strong>{session.topic}</strong></div>
    <div class="mode-switch" aria-label="Presentation switcher">
      <button class:chosen={morphology === 'atlas'} on:click={() => switchMorphology('atlas')}>A <span>ATLAS</span></button>
      <button class:chosen={morphology === 'signal'} on:click={() => switchMorphology('signal')}>B <span>SIGNAL</span></button>
    </div>
    <button class="mobile-orbit" on:click={jumpToEnd} aria-label="Jump to live synthesis">●</button>
  </header>

  <aside class="rail" aria-label="Session navigation">
    {#each ['Brief', 'Debate', 'Evidence', 'Decisions'] as item}
      <button class:active={active === item} on:click={() => active = item}><b>{item.slice(0, 2).toUpperCase()}</b><span>{item}</span></button>
    {/each}
    <div class="rail-bottom"><small>SESSION</small><strong>MM—2048</strong><em>LIVE</em></div>
  </aside>

  <section class="scene" aria-label="MultiMind session">
    <div class="hero">
      <p class="eyebrow">A deliberation in progress <span></span> 04 agents</p>
      <h1>{morphology === 'atlas' ? 'The city is a living shoreline.' : 'COAST / <em>DECISION</em>'}</h1>
      <p class="hero-copy">A working room for decisions that must hold across agencies, decades, and rising water.</p>
      <div class="hero-meter"><span>SCROLL TO ENTER THE THREAD</span><i></i></div>
    </div>

    <div class="agent-field" aria-label="Agent progress">
      {#each session.agents as agent, i}
        <article class:waiting={agent.state === 'WAITING'} class:pending={agent.state === 'PENDING'} style={`--i:${i}`}>
          <div class="orbit"><i style={`--p:${agent.progress}%`}></i></div>
          <div><small>{agent.state}</small><strong>{agent.name}</strong><span>{agent.progress}% assembled</span></div>
        </article>
      {/each}
    </div>

    <div class="thread-frame">
      <div class="thread-head"><span>DELIBERATION / 08 EXCHANGES</span><span class="live-dot">LIVE</span><button on:click={() => expanded = !expanded}>{expanded ? 'COMPACT' : 'READING MODE'}</button></div>
      <div class:expanded class="thread" bind:this={thread} on:scroll={() => savedScroll = thread?.scrollTop ?? 0}>
        <div class="scroll-material" aria-hidden="true"><span>01</span><i></i><span>08</span></div>
        {#each messages as [author, body, role], i}
          <article class={`message ${role}`} style={`--n:${i}`}>
            <div class="message-index">{String(i + 1).padStart(2, '0')}</div>
            <div class="message-body"><header><strong>{author}</strong><span>{role === 'human' ? 'ORIGIN' : role.toUpperCase()}</span><time>{9 + i}:2{i}</time></header><p>{body}</p></div>
          </article>
        {/each}
        <article class="live-response"><div class="pulse"></div><div><small>SYNTHESIS AGENT / FORMING RESPONSE</small><p>Weighing distributional impacts against the implementation horizon<span>.</span><span>.</span><span>.</span></p></div></article>
      </div>
      <div class="composer"><button on:click={() => notice = 'Context pin added to the live session'}>＋</button><span>Enter a perspective, constraint, or evidence request</span><kbd>⌘ ↵</kbd></div>
    </div>
  </section>

  <footer class="bottom-nav"><button on:click={() => active = 'Brief'}>BRIEF</button><button class="selected" on:click={() => active = 'Debate'}>DEBATE</button><button on:click={() => active = 'Evidence'}>EVIDENCE</button><button on:click={jumpToEnd}>LIVE <i></i></button></footer>
  <div class="toast" aria-live="polite">{notice}</div>
</main>
