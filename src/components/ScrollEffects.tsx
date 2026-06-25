"use client";

import { usePathname } from "next/navigation";
import { useEffect } from "react";

const revealSelector = [
  ".section-intro",
  ".benefit-card",
  ".sector-card",
  ".metric-card",
  ".mini-card",
  ".team-card",
  ".comparison-card",
  ".flow-card",
  ".visual-card",
  ".signature-card",
  ".cta-band-light",
  ".process-timeline__item",
  ".faq-accordion__item",
  ".contact-form",
  ".sector-detail",
].join(", ");

export function ScrollEffects() {
  const pathname = usePathname();

  useEffect(() => {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const elements = Array.from(document.querySelectorAll<HTMLElement>(revealSelector));

    if (prefersReducedMotion) {
      elements.forEach((element) => {
        element.classList.remove("reveal-ready");
        element.classList.add("reveal-in");
      });
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("reveal-in");
            observer.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px 0px -12% 0px", threshold: 0.12 },
    );

    elements.forEach((element, index) => {
      element.classList.add("reveal-ready");
      element.style.setProperty("--reveal-delay", `${(index % 5) * 45}ms`);
      observer.observe(element);
    });

    return () => {
      observer.disconnect();
    };
  }, [pathname]);

  return null;
}
