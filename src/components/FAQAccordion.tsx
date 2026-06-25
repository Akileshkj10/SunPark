"use client";

import { useState } from "react";
import type { FAQItem } from "@/content/types";

type FAQAccordionProps = {
  items: FAQItem[];
};

export function FAQAccordion({ items }: FAQAccordionProps) {
  const [openIndex, setOpenIndex] = useState(0);

  return (
    <div className="faq-accordion">
      {items.map((item, index) => {
        const isOpen = openIndex === index;
        const panelId = `faq-panel-${index}`;
        const buttonId = `faq-button-${index}`;

        return (
          <div className="faq-accordion__item" key={item.question}>
            <button
              aria-controls={panelId}
              aria-expanded={isOpen}
              className="faq-accordion__button"
              id={buttonId}
              onClick={() => setOpenIndex(isOpen ? -1 : index)}
              type="button"
            >
              <span>{item.question}</span>
              <span aria-hidden="true">{isOpen ? "-" : "+"}</span>
            </button>
            <div
              aria-labelledby={buttonId}
              className="faq-accordion__panel"
              hidden={!isOpen}
              id={panelId}
              role="region"
            >
              <p>{item.answer}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}
