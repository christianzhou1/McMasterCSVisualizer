interface ContainerProps {
  as?: React.ElementType;
  children: React.ReactNode;
  className?: string;
  id?: string;
}

export const Container = ({
  as: Element = "div",
  children,
  className,
  id,
  ...rest
}: ContainerProps) => {
  return (
    <Element
      id={id}
      {...rest}
      className={`flex flex-col w-full max-w-screen h-screen m-auto bg-white text-black ${className}`}
    >
      {children}
    </Element>
  );
};
