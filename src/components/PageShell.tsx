import type { ReactNode } from "react";
import { Footer } from "./Footer";
import { PageTransition } from "./PageTransition";
import { ScrollEffects } from "./ScrollEffects";
import { TopNav } from "./TopNav";

export function PageShell({ children }: { children: ReactNode }) {
  return (
    <>
      <a className="skip-link" href="#main-content">
        Skip to main content
      </a>
      <ScrollEffects />
      <TopNav />
      <PageTransition>
        <main id="main-content">{children}</main>
      </PageTransition>
      <Footer />
    </>
  );
}
