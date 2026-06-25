import type { Sector } from "@/content/types";

type SectorCardProps = {
  sector: Sector;
};

export function SectorCard({ sector }: SectorCardProps) {
  return (
    <article className="sector-card">
      <p className="type-caption sector-card__label">{sector.name}</p>
      <h3 className="type-title-lg">{sector.headline}</h3>
      <p>{sector.body}</p>
      <ul className="sector-card__list">
        {sector.suitability.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </article>
  );
}
