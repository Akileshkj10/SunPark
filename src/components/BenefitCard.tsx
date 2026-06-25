type BenefitCardProps = {
  body: string;
  title: string;
};

export function BenefitCard({ body, title }: BenefitCardProps) {
  return (
    <article className="benefit-card">
      <h3 className="type-title-sm">{title}</h3>
      <p>{body}</p>
    </article>
  );
}
